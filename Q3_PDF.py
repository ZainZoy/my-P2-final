from Q3 import *


class PDF_Document(Document):
    def __init__(self, f_name, f_size, content):
        super().__init__(f_name, f_size, content)
        self.name = f_name
        self.size = f_size
        self.content = content

    def open_file(self):
        return f"The file {self.name} is open and it is a PDF document."

    def read_file(self):
        return f"The file {self.name} is being read, and the content in this PDF document are : {self.content}"

    def save_file(self):
        return f"The file {self.name} is being saved as a PDF document and it's size is {self.size}."
