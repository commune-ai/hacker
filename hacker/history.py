import commune as c
import time

class History(c.Module):

    def __init__(self, 
                 max_tokens=420000, 
                 path='history',
                **kwargs):
        self.path = path
        self.max_tokens = max_tokens
    
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

    def get_files(self, path=None):
        path = path or './'
        return c.glob(path)
    
    def add_data(self,data, path=None):
        if not path:
            path = self.path + '/' + str(time.time())
        return self.put(path, data)
    
    def rm_data(self, path):
        return self.rm(path)
