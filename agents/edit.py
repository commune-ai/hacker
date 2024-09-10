import commune as c
from .base import Base

class Summarizer(Base):

    prompt = """

        -- OBJECTIVE --
        - edit the folder or file and write it while optimizing the code
        - you can add files to the folder or edit the files in the folder
        - you can also edit the file in the path
        - if you want to delete a file, you can do that as well by 

        --FORMAT--
        <{file_start}(path/to/file)> # start of file
        <{file_end}(path/to/file)> # end of file

        --TOOLS--
        TO CALL A TOOL, DO THE FOLLOWING
        @TOOL(TOOLNAME)> # start of tool
        
                
        -- CONTEXT --
        {context}
        
        """
    
    @c.endpoint()
    def generate(self, 
                path = __file__ ,
                 text='make a nextjs folder app that wraps over the generate funciton as if its a web app',
                temperature= 0.5,
                max_tokens= 1000000,
                model= 'anthropic/claude-3.5-sonnet',
            stream=True):
        text = self.process_text(text=text,context=path)
        return self.model.generate(text, stream=stream, model=model, max_tokens=max_tokens, temperature=temperature)
        
    def process_text(self, text, context=None):
        prompt = self.prompt
        context_content = ''
        assert c.exists(self.resolve_path(context)), f'Context path {context} does not exist'
        file2content = self.file2content(context)
        for file, content in file2content.items():
            context_content += f'<{self.file_start}({file})>'
            context_content += content
            context_content += f'<{self.file_end}({file})>'
            print(context_content)
        prompt = prompt.format(file_start=self.file_start, file_end=self.file_end, context = context_content)
        text = prompt + '\n' + text
        return text
    
    