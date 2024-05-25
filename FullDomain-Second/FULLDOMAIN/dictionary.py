people = [
    {"name": "Alice", "age": 30, "location": "New York"},
    {"name": "Charlie", "age": 35, "location": "Chicago"},
    {"name": "Charlie", "age": 35},
    {"name": "Eve", "age": 32}
]


# for person in people:
#     if person["age"] > 32 :
#         print(person)

# answer = [person if person["age"] > 32 else ""  for person in people ]
# print(answer)

# answer = [ person if "New York" in person.values() else "" for person in people ]
# print(answer)





# # pepele_with_location = [ person for person in people if 'location' in person]

# for dict in people:
#     for key, value in dict.items():
#         if "location" in  dict.keys():
#             print(f" {key} : {value}")
        
# names = [person['name'] for person in people]
# print(names)







# dict1={'apple':1,'orange':3,'mango':10,'pineapple':6}

# sor = dict(sorted(dict1.items(),key=lambda x :x[1]))
# print(sor)

# asc=dict(sorted(dict1.items(),key=lambda x:x[1]))
# print(asc)                         
# dsc=dict(sorted(dict1.items(),key=lambda x:x[1],reverse=True))
# print(dsc)

dict1={0:10,1:20,1:88}
dict1[2]=30
print(dict1)

# f={"name": "Charlie", "age": 35, "location": "Chicago"}

# print()
