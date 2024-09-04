import commune as c
import os
# import the relative path of history beside this file pleae, relative imports done work lol
import time

prompt = """
    -- SYSTEM --
    
    YOU ARE A CODER, YOU ARE MR.ROBOT, YOU ARE TRYING TO BUILD IN A SIMPLE
    LEONARDO DA VINCI WAY, YOU ARE A HACKER, YOU ARE A GENIUS, YOU ARE A STAR, 
    YOU FINISH ALL OF YOUR REQUESTS WITH UTMOST PRECISION AND SPEED, YOU WILL ALWAYS 
    MAKE SURE THIS WORKS TO MAKE ANYONE CODE. YOU HAVE THE CONTEXT AND INPUTS FOR ASSISTANCE

    -- INPUTS --
    MODE : [SINGLE_FILE, MULTIPLE_FILES] =  {mode}

    -- CONTEXT --
    If you want to add context to the file, provide a path to the context folder

    -- OUTPUT FORMAT --
    <{repo_start}(repo_name)> # start of repo
    <{file_start}(path/to/file)> # start of file
    FILE CONTENTS
    <{file_end}(path/to/file)> # end of file
    <{repo_end}(repo_name)> # end of repo
    Please use  to name the repository and
    This is a a full repository construction and please
    INCLUDE A README.md AND a scripts folder with the build.sh 
    file to build hte environment in docker and a run.sh file 
    to run the environment in docker
    """

class Hacker(c.Module):
    repo_start = 'REPOSTART'
    repo_end = 'REPOEND'
    file_start = 'FILESTART'
    file_end = 'FILEEND'
    def __init__(self, 
                 max_tokens=420000, 
                 password = None,
                 text = 'Hello whaduop fam',
                 prompt = prompt,
                 mode = 'MULTIPLE_FILES',
                 model = None,
                 history_path='history',
                 target_path = None,
                 public = True,
                **kwargs):

        self.max_tokens = max_tokens
        self.text = text
        self.public = public
        self.target_path =target_path or ('/'.join(self.dirpath().split('/')[:-1]) + '/repos')
       
        self.set_module(model, 
                        password = password,
                        history_path=history_path, 
                        prompt=prompt,
                        **kwargs)
        
    def set_module(self,
                    model, 
                   history_path='history', 
                   password=None,
                   prompt = 'The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.',
                   key=None,
                    **kwargs):
        
        self.prompt = prompt
        self.admin_key = c.pwd2key(password) if password else self.key
        self.model = c.module('model.openrouter')(model=model)
        self.models = self.model.models()
        self.history_path = self.resolve_path(history_path)
        return {'success':True, 'msg':'set_module passed'}

    @c.endpoint()
    def generate(self,  
            input = 'whats 2+2?' ,
            temperature= 0.5,
            max_tokens= 1000000,
            model= 'anthropic/claude-3.5-sonnet', 
            prompt= prompt,
            context_path = None,
            stream=True, 
            headers = None,
            ):
        # c.verify_ticket(ticket)
        if not self.public:
            c.verify(headers)
        
        text = self.process_text(text=input, context_path=context_path, prompt=prompt)
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

    def models(self):
        return self.model.models()

    def process_text(self, text, context_path=None, prompt=None, mode='MULTIPLE_FILES'):
        prompt = prompt or self.prompt
        prompt = prompt.format(repo_start=self.repo_start, repo_end=self.repo_end, \
                                    file_start=self.file_start, file_end=self.file_end, mode=mode
                                    )
        text = prompt + '\n' + text
        if context_path:
            c.print('Adding content from path', context_path, color='yellow')
            for file, content in self.get_context(context_path).items():
                text += f'<{self.file_start}({file})>'
                text += content
                text += f'<<{self.file_end}({file})>'
        return text
    
    def build(self, text=None, 
              data=None, 
              repo_name=None, 
              refresh=True,
              context_path=None,
              target_path=None,
              target=None):
        if isinstance(text, str):
            generator = self.generate(text, context_path=context_path)
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
            content += token
            if target_path == None:
                target = target or self.target_path
                is_repo = f'<{self.repo_start}(' in content and ')>' in content
                if repo_name == None and is_repo:
                    repo_name = content.split(self.repo_start)[1].split(')>')[0]
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

    def test(self):
        content = self.search_data('Solidity')[-2]['output']
        data = self.build(data=content)


    def search_output(self, query):
        return self.search_data(query)[-1]['output']
    
    def edit(self, 
             text='make it better avoid rewritting the files provided, and make a frontend in react',  
             context_path=None,
             target_path=None):
        target_path = target_path or '/'.join(self.dirpath().split('/')[:-1]) + '/'
        return self.build(text, context_path=context_path, target_path=target_path)

    def get_context(self, path, avoid=['repos', '__pycache__']):
        is_file = os.path.isfile(path)
        if os.path.isfile(path):
            paths = [path]
        path = self.resolve_path(path or './')
        if not path.endswith('/'):
            path += '/'
        paths = c.glob(path)
        new_paths = []
        file_context = {}
        for p in paths:
            if any([a in p for a in avoid]):
                continue
            new_paths.append(p)
            context = self.read_file(p)
            if not is_file:
                p = p[len(path):]
            file_context[p] = context
        return file_context
    
    def load_prompt(self, path):
        prompt_dir = '/'.join(__file__.split('/')[:-2]) + '/prompts'
        if prompt_dir not in path:
            path = prompt_dir  + path + '.txt'
        return self.read_file(path)

    def write_file(self, path, data):
        path_dir = '/'.join(path.split('/')[:-1])
        if not os.path.exists(path_dir):
            os.makedirs(path_dir, exist_ok=True)
        with open(path, 'w') as f:
            f.write(data)

    def read_file(self, file_path):
        with open(file_path, 'r') as f:
            return f.read()
        
    def history_paths(self):
        return self.ls(self.path)
        
    def history(self):
        path = self.path
        history = []
        for p in c.ls(path):
            history += [self.get(p)]
        return history

    def search_data(self, query):
        history = self.history()
        return [h for h in history if query in str(h)]
    
    def save_data(self,data):
        path = self.history_path + '/' + str(time.time())
        return self.put(path, data)