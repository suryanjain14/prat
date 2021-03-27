from abc import ABC, abstractmethod


class abs(ABC):

    @abstractmethod
    def method(self):
        pass


class abs2(ABC):
    def method(self):
        pass


ob = abs2()


class test:
    @abstractmethod
    def ts(self):
        pass


ob2 = test()


#     if you define @abstractmethod and class inherits from ABC then it becomes the abstract class
#     and its obj cant be created. (@abstractmethod and ABC ka poora khel hai babu bhaiya)

class sub(abs):

    def method(self):
        print('asd')


obj = sub()
obj.method()
# ob2 = abs()
