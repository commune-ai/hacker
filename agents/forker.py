import commune as c
import os
agent = c.module('agent')
class Forker(agent):
    def edit(self, 
             text='make it better avoid rewritting the files provided, and make a frontend in react', 
             path = None):
        path  = self.resolve_path(path or c.pwd())
        return self.generate(text, context_path=path)