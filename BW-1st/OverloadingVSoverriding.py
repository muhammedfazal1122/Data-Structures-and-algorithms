############################## method Overloading:


class aaaddd:
    def addition(self, a,b=0,c=0):
        return a+b+c
    
    def summ(self, *args):
        return sum(args)
    

a =  aaaddd()
# print(a.addition(2))
# print(a.summ(2,4,4,66,6666))
# print(a.summ(2))


################################## metodoverriding 

class Animal:
    def sound(self):
        return "animals sounts"
    
class Dog:
    def sound(self):
        return "booww boww"
    
class Cat:
    def sound(self):
        return "mweaaooo"

animal = Animal()
# print(animal.sound())
# dog  = Dog()
# print(dog.sound())