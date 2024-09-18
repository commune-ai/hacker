import hacker as h

class Summarizer(h.Module):

    prompt = """
        -- OBJECTIVE --
        - include all import paths and their schema and include input and output format for the model to understand
        - If you want to add context to the file, provide a path to the context folder
        - an exampel of a funciton would be fn >> inputs(inputs) -> outputs(outputs)
        - include all of the types like for linting
        - if it is a class or object oriented code, include the class and the methods and the attributes
        - if the user is asking a question about it, follow their instructions, if you need to generate files that would help the repo
        -- CONTEXT --
        {context}
        -- FILE OUTPUT/INPUT FORMAT --
        <{file_start}(path/to/file)> # start of file
        <{file_end}(path/to/file)> # end of file
        """
    def __init__(self, 
                 max_tokens=420000, 
                file_start = 'FILE_START',
                file_end = 'FILE_END',
                path='history',
                 password = None,
                 model = None,
                 target_path = None,
                 public = True,
                **kwargs):
        self.file_start = file_start
        self.file_end = file_end
        self.max_tokens = max_tokens
        self.public = public
        self.target_path =target_path or ('/'.join(self.dirpath().split('/')[:-1]) + '/repos')
        self.admin_key = h.pwd2key(password) if password else self.key
        self.model = h.module('model.openrouter')(model=model)
        self.models = self.model.models()
        self.set_history_path(path)

    def generate(self,  
            text = 'Summarize the code' ,
            temperature= 0.5,
            max_tokens= 1000000,
            model= 'anthropic/claude-3.5-sonnet', 
            context = __file__,
            prompt= prompt,
            stream=True, 
            headers = None,
            ):

        if not self.public:
            h.verify(headers)

        text = self.process_text(text=text,context=context)

        response =  self.model.generate(text,
                                        stream=stream, 
                                        model=model, 
                                        max_tokens=max_tokens, 
                                        temperature=temperature)
        output = ''
        try:
            for token in response:
                output += token
                yield token
        except Exception as e:
            output = h.detailed_error(e)

        data = {
            'input': text, 
            'output': output, 
            'max_tokens': max_tokens, 
            'temperature': temperature,
            'prompt': prompt,
            'headers': headers
        }
        self.save_data(data)
        yield {'success':True, 'msg':'done', 'data_hash':h.hash(data)}

    def process_text(self, text, context=None):
        prompt = self.prompt
        context_content = ''
        assert h.exists(self.resolve_path(context)), f'Context path {context} does not exist'
        print('Adding content from path', context)
        file2content = self.file2content(context)
        print(file2content, 'FAMMMM')
        for file, content in file2content.items():
            context_content += f'<{self.file_start}({file})>'
            context_content += content
            context_content += f'<{self.file_end}({file})>'
            print(context_content)
        prompt = prompt.format(file_start=self.file_start, file_end=self.file_end, context = context_content)
        text = prompt + '\n' + text
        print(text, 'FAM', self.prompt)
        return text