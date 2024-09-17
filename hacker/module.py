import commune as c
import time
import os

class Base(c.Module):
    public = True
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

    repo_start = 'REPO_START'
    repo_end = 'REPO_END'
    file_start = 'FILE_START'
    file_end = 'FILE_END'

    def __init__(self, 
                 max_tokens=420000, 
                 password = None,
                 model = None,
                 history_path='history',
                 target = None,
                 public = True,
                **kwargs):
        
        self.max_tokens = max_tokens
        self.public = public
        self.target = target or  ('/'.join(self.dirpath().split('/')[:-1]) + '/repos')
        self.set_model(model, password=password, history_path=history_path, **kwargs)

    def set_history_path(self, path):
        self.path = c.resolve_path(path)
    def history_paths(self):
        return c.ls(self.path)
    
    def history(self):
        return [self.get(p) for p in self.history_paths()]
    
    def search_data(self, query):
        history = self.history()
        return [h for h in history if query in str(h)]

    def save_data(self,data, path=None):
        if not path:
            path = self.path + '/' + str(time.time())
        else:
            path = self.path + '/' + path
        return self.put(path, data)
    
    def rm_data(self, path):
        path = self.resolve_path(path)
        return self.rm()

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
        path = self.path + '/' + str(time.time())
        return self.put(path, data)

    def models(self):
        return self.model.models()
    
    def is_file(self, path): 
        return os.path.isfile(path)

    def file2content(self, path, avoid=['__pycache__']):
        if not os.path.exists(str(path)):
            return {}
        path = c.resolve_path(path or './')
        is_file = os.path.isfile(path)
        paths = [path] if is_file else c.glob(path)
        new_paths = []
        file_context = {}
        for p in paths:
            if any([a in p for a in avoid]):
                continue
            new_paths.append(p)
            print(p)
            context = self.read_file(p)
            if not is_file:
                p = p[len(path):]
            file_context[p] = context
        return file_context
    
    def set_model(self,
                    model=None, 
                   history_path='history', 
                   password=None,
                    **kwargs):
        
        self.admin_key = c.pwd2key(password) if password else self.key
        self.model = c.module('model.openrouter')(model=model)
        self.models = self.model.models()
        self.history_path = self.resolve_path(history_path)
        c.print('Set model', model, color='yellow')
        return {'success':True, 'msg':'set_module passed'}


    def prompt_args(self):
        # get all of the names of the variables in the prompt
        prompt = self.prompt
        variables = []
        for line in prompt.split('\n'):
            if '{' in line and '}' in line:
                variable = line.split('{')[1].split('}')[0]
                variables.append(variable)

        return variables

    def build(self, text=None, 
              data=None, 
              repo_name=None, 
              refresh=True,
              target=None,
              context=None):
        target = target or self.target
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
            repo_start =  f'<{self.repo_start}('
            is_repo = repo_start in content and ')>' in content
            if target == None:
                target = self.target
            if repo_name == None and is_repo:
                repo_name = content.split(repo_start)[1].split(')>')[0]
                target = target + '/' + repo_name
                if not os.path.exists(target):
                    os.makedirs(target, exist_ok=True)
                if os.path.exists(target) and refresh:
                    c.print('Refreshing repo', target, color='yellow')
                    c.rm(target)
                c.print(buffer, 'CREATING REPO --> ', repo_name, buffer,color=color)

            file_start = f'<{self.file_start}('
            file_end = f'<{self.file_end}('
            is_file_in_content =  content.count(file_start) == 1 and content.count(file_end) == 1
            c.print(token, end='', color=color)
            if is_file_in_content:
                file_path = content.split(file_start)[1].split(')>')[0]
                file_path_tag = f'{file_start}{file_path})>'
                file_content = content.split(file_path_tag)[1].split(file_end)[0]
                self.write_file(target + '/' + file_path, file_content)
                c.print(buffer,'Writing file --> ', file_path, buffer, color=color)
                content = ''
                color = c.random_color()
        
        return file2content

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



    def process_text(self, text, context=None):
        prompt = self.prompt
        c.print('Adding content from path', context, color='yellow')
        context = c.file2text(context) if context else ''
        print(context, 'CONTEXT')
        prompt = prompt.format(file_start=self.file_start, 
                               file_end=self.file_end,
                               repo_start=self.repo_start,
                               repo_end=self.repo_end,
                                 context = context)
        text = prompt + '\n' + text
        return text
    

    gen = generate