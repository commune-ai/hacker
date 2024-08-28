import commune as c
import streamlit as st
st.write(c.pwd())
import os
# import the relative path of history beside this file pleae, relative imports done work lol

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


class Chat(c.Module):

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

        return {'success':True, 'msg':'set_module passed'}

    @c.endpoint()
    def generate(self,  
            input = 'whats 2+2?' ,
            temperature= 0.5,
            max_tokens= 1000000,
            model= 'anthropic/claude-3.5-sonnet', 
            prompt= prompt,
            files = None,
            stream=True, 
            headers = None,
            ):
        # c.verify_ticket(ticket)
        if not self.public:
            c.verify(headers)
        
        text = self.process_text(input, files=files)
        response =  self.model.generate( text,stream=stream, model=model, max_tokens=max_tokens, temperature=temperature )
        data = {
            'input': input, 
            'output': '', 
            'max_tokens': max_tokens, 
            'temperature': temperature,
            'prompt': prompt,
            'headers': headers
        }
        for token in response:
            data['output'] += token
            yield token
        self.history_module.add_data(data)
        yield 'done'

    def ask(self, *text, **kwargs): 
        return self.generate(' '.join(text), **kwargs)
    def code(self, *text, **kwargs):
        return self.generate(' '.join(text), **kwargs)
    
    def models(self):
        return self.model.models()
    
    def process_text(self, text, files=None):
        text = self.prompt + '\n' + text
        if files:
            if isinstance(files, str):
                files = [files]
            text += '\n USE THE FOLLOWING TO WRITE FILES'
            for file in files:
                text += f'<file({file})>'
                text += self.read_file(file)
                text += f'<file({file})>'

        return text
    

    def read_file(self, file_path):
        with open(file_path, 'r') as f:
            return f.read()
        

    def build(self, text=None, 
              data=None, 
              repo_name=None, 
              refresh=True,
              target=None):
        target = target or self.target_path

        if isinstance(text, str):
            generator = self.generate(text)
        elif isinstance(data, str):
            generator = data
        else:
            raise ValueError('Please provide a text or data string')
        # generator = self.search_output('app')
        content = ''
        file_path = None
        file2content = {}

        file_open = False
        repo_path = None
        line = ''
        
 
        line_index = 0
        for token in generator:
            content += token
            is_repo = '<repo(' in content and ')>' in content
            if repo_name == None and is_repo:
                repo_name = content.split('<repo(')[1].split(')>')[0]
                repo_path = target + '/' + repo_name
                if not os.path.exists(repo_path):
                    os.makedirs(repo_path, exist_ok=True)
                if os.path.exists(repo_path) and refresh:
                    c.print('Refreshing repo', repo_path, color='yellow')
                    c.rm(repo_path)

                    
                    # c.rm(target)
                c.print('Writing repo --> ', repo_name, color='green')
            
            if content.count('<file(') == 2 and content.count(')>') == 2:
                file_open = False
                file_path = content.split('<file(')[1].split(')>')[0]
                file_path_tag = f'<file({file_path})>'
                file_content = content.split(file_path_tag)[1].split('<file(')[0]
                print('file_content', file_content, file_path)
                assert repo_path, 'Please provide a repo name'
                self.write_file(repo_path + '/' + file_path, file_content)
                c.print('Writing file --> ', file_path, color='green')
                content = ''
        
        return file2content
    


    def edit_file(self, file_path, content):
        with open(file_path, 'w+') as f:
            f.write(content)
        return True
    

    def test(self):
        content = self.search_data('Solidity')[-2]['output']
        data = self.build(data=content)


    def write_file(self, path, data):
        path_dir = '/'.join(path.split('/')[:-1])
        if not os.path.exists(path_dir):
            os.makedirs(path_dir, exist_ok=True)
        with open(path, 'w') as f:
            f.write(data)


    def search_output(self, query):
        return self.search_data(query)[-1]['output']
    

    def edit_file(self, text='make it better',  files=None):
        files = files or self.get_files()
        return self.generate(text, files=files)
    
    def get_files(self, path=None, avoid=['repos', '__pycache__']):
        path = path or './'
        paths = c.glob(path) 
        new_paths = []
        for p in paths:
            if any([a in p for a in avoid]):
                continue
            new_paths.append(p)
        return new_paths
