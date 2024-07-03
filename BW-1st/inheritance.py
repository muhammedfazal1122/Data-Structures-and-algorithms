# class Animal:

#     name = "Animaalll"

#     def sound(self):
#         sss = "Animal sound()"
#         return "animalss souuunnndddd"
    
# class Dog (Animal):
#     name = 'Dog'
    
#     def sound(self):
#         dogSound = 'child dog sound'
#         return "doooogg sounddd",dogSound
#     def soo(self):
#         return "soooooooooo"
    
# patti = Dog()
# print(patti.sound())
# print(super(Dog,patti).name)




class Animal:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
    def __add__(self,other):
        return self.a +other.a, self.b + other.b

aaaa = Animal(1,2)
bbbb = Animal(4,3)
print(aaaa + bbbb)



