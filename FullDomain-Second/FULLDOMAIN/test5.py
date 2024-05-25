# d={1:10,2:11}
#
# b=d[1]
# c=d[2]
# d[1]=c
# d[2]=b
# print(d)
#
# a = 10
# b = 10
# c = a
# d = b
# a = d
# b = c
#
#
# def decorator(fun):
#     def operation(a,b):
#         if b==0:
#             print('division not possible')
#         else:
#             return fun(a,b)
#
#     return operation
#
#
# @decorator
# def division(a,b):
#     return a/b
#
# s=division(10,30)
# print(s)
#
#
#
# d={1:10,2:11}
# d[3]=12
# print(d)
# d2={4:10,9:11,7:33,1:55,5:12}
#
# print(sum(d2.values()))


# for k,v in d2.items():
#     print(f"key={k} and value = {v}")
# n=5
# s={n:n*n for n in range(1,n+1)}
# print(s)


# s=sorted(d2.items(),key=lambda x:x[0])
# print(dict(s))
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
#
# dic1.update(dic2)
# dic1.update(dic3)
#
# print(dic1)


# people = [
#     {"name": "Alice", "age": 30, "location": "New York"},
#     {"name": "Charlie", "age": 35, "location": "Chicago"},
#     {"name": "Charlie", "age": 35},
#     {"name": "Eve", "age": 32}
# ]
#
# # sorting based on age
#
# s=sorted(people,key=lambda x:x["age"])
# print(s)
#
# # printing first elements using fstring
#
# print(f"name={people[0]['name']} ")
#
# # filter elements using list comprehension or printing the field contain location or not contain location
#
# f=[i for i in people if "location" in i]
# print(f)
#
# # print alice data by looping
#
# for i in people[0]:
#     print(i)
#     print(people[0][i])
#
#
# # printing name and values seperately
#
# s={"name": "Alice", "age": 30, "location": "New York"}
#
# for k,v in s.items():
#     print(f"key={k} and value={v}")


# d = {'seven': 7,'two': 2,'nine': 9,'four': 4,'ten': 10,'five': 5, 'five': 5}
# result={}
# for k,v in d.items():
#     if v not in result.values():
#         result[k]=v
# print(result)

# d={1:10,2:20,3:30,4:40,5:50}
#
# d1={v:k for k,v in d.items()}
# print(d1)


try:
    x = 10
    y = 20
    
except SyntaxError as e:
    print(f"sytaxerror{e}")





