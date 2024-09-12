import commune as c
import os

from .base import Base
# import the relative path of history beside this file pleae, relative imports done work lol

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

class Hacker(Base):
    prompt = prompt
   
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
    