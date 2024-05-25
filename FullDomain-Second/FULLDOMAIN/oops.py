# #inheritance
#
# class greet:
#     def hello(self):
#         print('hello')
#
# class name(greet):
#     def name(self):
#         print('fazal')
#
# c=name()
# c.hello()
# c.name()
#

#.............................................polymorphism

#
# class bird:
#     def intro(self):
#         print('some birds can fly')
#
# class parrot(bird):
#     def intro(self):
#         print('parrot can fly')
#
# class ostrich(bird):
#     def intro(self):
#         print('ostrich cannot fly')
#
# b=bird()
# b.intro()
# p=parrot()
# p.intro()
# o=ostrich()
# o.intro()

#................................acess modifires

# class names:
#     def public(self):
#         print('this is public')
#
#     def _protected(self):
#         print('this protected')
#
#     def __private(self):
#         print('this is private')
#
# z=names()
# z.public()
# z._protected()
# z._names__private()

#...................................................super keyword

# class vehicle:
#     def start(self):
#         print('vehicle started')
#
# class car(vehicle):
#     def start(self):
#         super().start()
#         print('car started')
#
# s=car()
# s.start()

