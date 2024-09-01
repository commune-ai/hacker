import commune as c
import os
agent = c.module('hacker')
prompt = c.get_text(c.pwd() + '/prompts/spawner.txt')


class Forker(agent):
    def edit(self, 
             text='make this', 
             path = None):
        # path  = self.resolve_path(path or c.pwd())
        return self.build(prompt, context_path=path)