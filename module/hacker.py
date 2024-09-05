import commune as c
from .base import Base
import os
# import the relative path of history beside this file pleae, relative imports done work lol
import time


class Hacker(Base):

    prompt = """
        -- SYSTEM --
        
        YOU ARE A CODER, YOU ARE MR.ROBOT, YOU ARE TRYING TO BUILD IN A SIMPLE
        LEONARDO DA VINCI WAY, YOU ARE A HACKER, YOU ARE A GENIUS, YOU ARE A STAR, 
        YOU FINISH ALL OF YOUR REQUESTS WITH UTMOST PRECISION AND SPEED, YOU WILL ALWAYS 
        MAKE SURE THIS WORKS TO MAKE ANYONE CODE. YOU HAVE THE CONTEXT AND INPUTS FOR ASSISTANCE

        - Please use  to name the repository and
        - This is a a full repository construction and please
        - INCLUDE A README.md AND a scripts folder with the build.sh 
        - file to build hte environment in docker and a run.sh file 
        - to run the environment in docker
        - INCLUDE A TESTS folder for pytests

        -- CONTEXT --
        {context}
        -- OUTPUT FORMAT --
        <{repo_start}(repo_name)> # start of repo
        <{file_start}(path/to/file)> # start of file
        FILE CONTENTS
        <{file_end}(path/to/file)> # end of file
        <{repo_end}(repo_name)> # end of repo

        """

    def __init__(self, 
                 max_tokens=420000, 
                 password = None,
                 text = 'Hello whaduop fam',
                 model = None,
                 history_path='history',
                 target_path = None,
                 public = True,
                repo_start = 'REPO_START',
                repo_end = 'REPO_END',
                file_start = 'FILE_START',
                file_end = 'FILE_END',
                **kwargs):


        self.repo_start = repo_start
        self.repo_end = repo_end
        self.file_start = file_start
        self.file_end = file_end

        self.max_tokens = max_tokens
        self.text = text
        self.public = public
        self.target_path =target_path or ('/'.join(self.dirpath().split('/')[:-1]) + '/repos')
        self.set_model(model, 
                        password = password,
                        history_path=history_path, 
                        **kwargs)
        
    @c.endpoint()
    def generate(self,  
            input = 'whats 2+2?' ,
            temperature= 0.5,
            max_tokens= 1000000,
            model= 'anthropic/claude-3.5-sonnet', 
            prompt= prompt,
            context = None,
            stream=True, 
            headers = None,
            ):
        # c.verify_ticket(ticket)
        if not self.public:
            c.verify(headers)
        
        text = self.process_text(text=input, context=context)
        response =  self.model.generate( text,stream=stream, model=model, max_tokens=max_tokens, temperature=temperature )
        data = {
            'input': input, 
            'output': '', 
            'max_tokens': max_tokens, 
            'temperature': temperature,
            'prompt': prompt,
            'headers': headers
        }
        try:
            for token in response:
                data['output'] += token
                yield token
            self.save_data(data)
        except Exception as e:
            yield None
        yield 'done'

    def build(self, text=None, 
              data=None, 
              repo_name=None, 
              refresh=True,
              target_path=None,
              target=None, 
              context=None):
        if isinstance(text, str):
            generator = self.generate(text, context=context )
        elif isinstance(data, str):
            generator = data
        else:
            raise ValueError('Please provide a text or data string')
        # generator = self.search_output('app')
        content = ''
        file_path = None
        file2content = {}
        buffer = '-------------'
        color = c.random_color()
        print('Building repo')
        for token in generator:
            content += str(token)
            if target_path == None:
                target = target or self.target_path
                repo_start =  f'<{self.repo_start}('
                is_repo = repo_start in content and ')>' in content
                if repo_name == None and is_repo:
                    repo_name = content.split(repo_start)[1].split(')>')[0]
                    target_path = target + '/' + repo_name
                    if not os.path.exists(target_path):
                        os.makedirs(target_path, exist_ok=True)
                    if os.path.exists(target_path) and refresh:
                        c.print('Refreshing repo', target_path, color='yellow')
                        c.rm(target_path)
                    c.print(buffer, 'CREATING REPO --> ', repo_name, buffer,color=color)
            # is file entirely in the content

            # anchors for the file where 
            # <FILESTART(path/to/file)> content <FILEEND(path/to/file)>
            file_start = f'<{self.file_start}('
            file_end = f'<{self.file_end}('
            is_file_in_content =  content.count(file_start) == 1 and content.count(file_end) == 1
            c.print(token, end='', color=color)
            if is_file_in_content:
                file_path = content.split(file_start)[1].split(')>')[0]
                file_path_tag = f'{file_start}{file_path})>'
                file_content = content.split(file_path_tag)[1].split(file_end)[0]
                assert target_path, 'Please provide a repo name'
                self.write_file(target_path + '/' + file_path, file_content)
                c.print(buffer,'Writing file --> ', file_path, buffer, color=color)
                content = ''
                color = c.random_color()
        
        return file2content
    


    def prompt_args(self):
        # get all of the names of the variables in the prompt
        prompt = self.prompt
        variables = []
        for line in prompt.split('\n'):
            if '{' in line and '}' in line:
                variable = line.split('{')[1].split('}')[0]
                variables.append(variable)

        return variables
