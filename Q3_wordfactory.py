from Q3_AbFactory import *
from Q3_word import *


class Word_Factory(DocumentFactory):
    def create_document(self):
        f_name = input("enter name: ")
        f_size = input("enter the file size: ")
        content = input("enter the content inside it: ")
        return Word_Document(f_name, f_size, content)
