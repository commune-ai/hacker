import commune as c
import streamlit as st
import os
# import the relative path of history beside this file pleae, relative imports done work lol
from .storage import Storage
from .history import History

prompt = """

    The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.
    
    If you are a coder, write the files as such
    Please use <repo(repo_name)> to name the repository and
    <file(path/to/file)>
    {file contents}
    <file(path/to/file)>

    This is a a full repository construction and please

    INCLUDE A README.md AND a scripts folder with the build.sh file to build hte environment in docker and a run.sh file to run the environment in docker
    """


class Hacker(c.Module):

    def __init__(self, 
                 max_tokens=420000, 
                 password = None,
                 text = 'Hello whaduop fam',
                 prompt = prompt,
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
        self.history_module = History(path= self.resolve_path(history_path))
        self.search_data = self.history_module.search_data
        self.history = self.history_module.history
        self.storage = Storage(path='storage')
        return {'success':True, 'msg':'set_module passed'}

    @c.endpoint()
    def generate(self,  
            input = 'whats 2+2?' ,
            temperature= 0.5,
            max_tokens= 1000000,
            model= 'anthropic/claude-3.5-sonnet', 
            prompt= prompt,
            context_path = None,
            repo_path = None,
            stream=True, 
            headers = None,
            ):
        # c.verify_ticket(ticket)
        if not self.public:
            c.verify(headers)
        
        text = self.process_text(input, context_path=context_path)
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
            self.history_module.add_data(data)
        except Exception as e:
            yield None
        yield 'done'

    def models(self):
        return self.model.models()

    def process_text(self, text, context_path=None):
        text = self.prompt + '\n' + text
        if context_path:
            c.print('Adding content from path', context_path, color='yellow')
            for file, content in self.get_context(context_path).items():
                text += f'<file({file})>'
                text += content
                text += f'<file({file})>'
        return text
    
    def build(self, text=None, 
              data=None, 
              repo_name=None, 
              refresh=True,
              context_path=None,
              repo_path=None,
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
        for token in generator:
            content += token
            if repo_path == None:
                target = target or self.target_path
                is_repo = '<repo(' in content and ')>' in content
                if repo_name == None and is_repo:
                    repo_name = content.split('<repo(')[1].split(')>')[0]
                    repo_path = target + '/' + repo_name
                    if not os.path.exists(repo_path):
                        os.makedirs(repo_path, exist_ok=True)
                    if os.path.exists(repo_path) and refresh:
                        c.print('Refreshing repo', repo_path, color='yellow')
                        c.rm(repo_path)
                    c.print(buffer, 'CREATING REPO --> ', repo_name, buffer,color=color)
            
            if content.count('<file(') == 2 and content.count(')>') == 2:
                
                
                file_path = content.split('<file(')[1].split(')>')[0]
                file_path_tag = f'<file({file_path})>'
                file_content = content.split(file_path_tag)[1].split('<file(')[0]
                assert repo_path, 'Please provide a repo name'
                self.storage.write_file(repo_path + '/' + file_path, file_content)
                c.print(buffer,'Writing file --> ', file_path, buffer, color=color)
                content = ''
                color = c.random_color()
            c.print(token, end='', color=color)
        
        return file2content
    


    def test(self):
        content = self.search_data('Solidity')[-2]['output']
        data = self.build(data=content)


    def search_output(self, query):
        return self.search_data(query)[-1]['output']
    

    def default_repo_path(self):
        return '/'.join(self.dirpath().split('/')[:-1]) + '/'

    def edit(self, 
             text='make it better avoid rewritting the files provided, and make a frontend in react',  
             context_path=None,
             repo_path=None):
        repo_path = repo_path or '/'.join(self.dirpath().split('/')[:-1]) + '/'
        return self.build(text, context_path=context_path, repo_path=repo_path)

    

     

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
            context = self.storage.read_file(p)
            if not is_file:
                p = p[len(path):]
            file_context[p] = context
        return file_context
    



    # def build_file(self, path, context_path=None):
        