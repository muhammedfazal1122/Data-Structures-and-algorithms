
######################### varialblessssssssss


class Variables:
    a = 20
    
    def __init__(self,value):
        self.value = value
        self.__private= 'immmm priiivate'


    def hello(self):
        a = 10
        self.a = 30
        self.value= 100001
        self.__private= 'priiivate'

        return self.a, a, self.value, Variables.a ,self.__private
    



vv = Variables(10)

print(vv.hello)