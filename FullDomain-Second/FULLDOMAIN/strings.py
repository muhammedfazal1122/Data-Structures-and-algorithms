# def charfrequency(c):
#     dict1={}
#     keys=dict1.keys()
#     for i in c:
#         if i in keys:
#             dict1[i]+=1
#         else:
#             dict1[i]=1
#     return dict1
#
# s=charfrequency('fazal')
# print(s)
# print(s.keys())

# def charfrequency(char):
#     dict1={}
#     keys=dict1.keys()
#     for i in char:
#         if i in keys:
#             dict1[i]+=1
#         else:
#             dict1[i]=1
#     return dict1
#
# s=charfrequency('fazal')
# print(s)

#........................reverse a string

# def reverse(s):
#     l=''
#     for i in s:
#         l=i+l
#     return l
# s=reverse('fazal')
# print(s)


#.............................slice..

# def cut(s):
#     if len(s) <2:
#         return ''
#     else:
#         return s[0:2]+s[4:]
# k=cut('fazal')
# print(k)

#..................change the first char

# def changechar(c):
#     newc=c[0]
#     for i in c[1:]:
#         if c[0]==i:
#             newc+='$'
#         else:
#             newc+=i
#     return newc
#
# s=changechar('mam')
# print(s)

# def swap(c1,c2):
#     return c2+''+c1
# print(swap('xyz','abc'))
#
#..........................................change string
# def string(s):
#     if 'ing' in s:
#         return s+'ly'
#     else:
#         return s+'ing'
#
# k=string('string')
# print(k)