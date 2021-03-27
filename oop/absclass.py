from abc import ABC, abstractmethod


class abs(ABC):

    @abstractmethod
    def method(self):
        pass


#     if you define @abstractmethod and class inherits from ABC then it becomes the abstract class
#     and its obj cant be created. (@abstractmethod ka poora khel hai babu bhaiya)

class sub(abs):

    def method(self):
        print('asd')


ob2 = abs()
