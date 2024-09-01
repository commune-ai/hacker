import commune as c
import os
# import the relative path of history beside this file pleae, relative imports done work lol
import time

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






class Actor(c.Module):

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

    def process_text(self, text, context_path=None, prompt=None):
        prompt = prompt or self.prompt
        text = prompt + '\n' + text
        if context_path:
            c.print('Adding content from path', context_path, color='yellow')
            for file, content in self.get_context(context_path).items():
                text += f'<file({file})>'
                text += content
                text += f'<file({file})>'
        return text

    def test(self):
        content = self.search_data('Solidity')[-2]['output']
        data = self.build(data=content)

    def search_output(self, query):
        return self.search_data(query)[-1]['output']
    

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
    
    def remove_all_data(self):
        # prompt are you sure
        return self.rm(self.history_path)
    
    def test(self):
        self.generate('whats 2+2?')
        