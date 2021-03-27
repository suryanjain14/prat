class Mobile:
    fp = 'yes'

    @classmethod
    def change(cls, val):
        cls.fp = val
        cls.new = "asdfsa"

    #     class method is used for interaction with class variables
    # it basically is of no use you can also access class variables using class Name

    def schange(self, val):
        self.fp = val

    @staticmethod
    def method(arg1, arg2):
        print(arg1, arg2)
        print(Mobile.fp)


#         static method can access the class variables and it is not
#  associated with the class or instance


obj = Mobile()
ob2 = Mobile()
obj.schange("as")
print(ob2.fp)
obj.change("chan")
print((ob2.new))
Mobile.method(1, 2)
