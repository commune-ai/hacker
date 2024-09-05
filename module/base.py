import commune as c
import time
import os



class Base(c.Module):

    def __init__(self, path='history'):
        self.set_history_path(path)
    
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
    
    def process_text(self, text, context=None):
        prompt = self.prompt
        context_content = ''
        assert c.exists(self.resolve_path(context)), f'Context path {context} does not exist'
        c.print('Adding content from path', context, color='yellow')
        for file, content in self.file2content(context).items():
            context_content += f'<{self.file_start}({file})>'
            context_content += content
            context_content += f'<{self.file_end}({file})>'
        prompt = prompt.format(file_start=self.file_start, 
                               file_end=self.file_end,
                               repo_start=self.repo_start,
                               repo_end=self.repo_end,
                                 context = context_content)
        text = prompt + '\n' + text
        print(text, 'FAM', self.prompt)
        return text
    
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
                    model, 
                   history_path='history', 
                   password=None,
                    **kwargs):
        
        self.admin_key = c.pwd2key(password) if password else self.key
        self.model = c.module('model.openrouter')(model=model)
        self.models = self.model.models()
        self.history_path = self.resolve_path(history_path)
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
