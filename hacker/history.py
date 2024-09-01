import commune as c
import time

class History(c.Module):

    def __init__(self, 
                 path='history',
                **kwargs):
        self.set_path(path)
        
    def set_path(self, path):
        self.path = c.resolve_path(path)
    
    def history_paths(self):
        return c.ls(self.path)
    
    def history(self):
        return [self.get(p) for p in self.history_paths()]
    
    def search_data(self, query):
        history = self.history()
        return [h for h in history if query in str(h)]

    def add_data(self,data, path=None):
        if not path:
            path = self.path + '/' + str(time.time())
        return self.put(path, data)
    
    def rm_data(self, path):
        return self.rm(path)
