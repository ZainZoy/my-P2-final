from Q3_wordfactory import *
from Q3_Excelfactory import *
from Q3_PDFfactory import *
from Q3_word import *
from Q3_PDF import *
from Q3_Excel import *

types_available = {
    "word": Word_Factory,
    "pdf": PDF_Factory,
    "excel": Excel_Factory
}


def driver():
    global types_available
    while True:
        user_input = input("what type of document do you want: ")
        user_input = user_input.lower()
        if user_input in types_available:
            temp_object = types_available[user_input]().create_document()
            print(f"your document is created of type {user_input}")
            return temp_object
        else:
            print("invalid type, it is not available.")


ob1 = driver()
print(ob1.open_file())
print(ob1.read_file())
print(ob1.save_file())
