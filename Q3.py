# Factory pattern

from abc import ABC, abstractmethod


class Document(ABC):
    def __init__(self, f_name, f_size, content):
        pass

    @abstractmethod
    def open_file(self):
        pass

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def save_file(self):
        pass



