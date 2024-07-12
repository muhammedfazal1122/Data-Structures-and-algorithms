# most rpt letter in a string
# ----------------------------------------------------------------------------------------


s = "abcaaaabba"
maxxstring = ''
maxx = 0
for i in range(len(s)):
    count = 1
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            count = count + 1
    
    if count > maxx:
        maxx = count
        maxxstring = s[i]

  


print(maxxstring)
print(maxx)

#  ----------------------------------------------------------------------------------------
    


def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


# Example usage
original_string = "hello"
reversed_string = reverse_string(original_string)
print(reversed_string)  


'''
-------------------------------------------------question -> flate a nested list 


'''
nested_list = [1, [2, [3, 4], 5], [6, 7], 8, [9, [10, 11]]]

def reverse_nested_list(lst):
    res = []
    for item in lst[::-1]:
        if type(item) ==  list:
            res.append(reverse_nested_list(item))
        else:
            res.append(item)
    return res

# Applying the function to the nested list
result = reverse_nested_list(nested_list)
print(result)

    
#  ----------------------------------------------------------------------------------------

a={"a":1,"b":[1,2,3],"c":[1,2],"d":2}


summ = 0 

for  val in a.values() :
    if type(val) == list:
        for i in val:
            summ += i
    else:
        summ += val


print(summ)



# ----------------------------------------------------------------------------------------



arr = {"a": {"b": {"c": 0}},
       "b": {"c": 1},
       "c": 2}


def rec(arr):
    summ = 0
    for i in  arr.values():
        if type(i) == dict:
            summ += rec(i)
        else:
            summ += i
    return summ
        

        
print(rec(arr))




# ----------------------------------------------------------------------------------------

s = "xoxyyoyydfgwdfopkpofdf"

count = 0

def is_palindrom(arr):
    return arr == arr[::-1]

for i in range(len(s)-2):
    for j in range(i+3, len(s)+1):
        if is_palindrom(s[i:j]):
            count += 1
      

print(count)


# ----------------------------------------Middleware-------------------------------------------------
from django.contrib.auth import logout
from django.shortcuts import redirect

class MiddlewareIsBlocked:

    def __init__(self,get_response) -> None:
        self.get_response = get_response

    def __call__(self,request):
        
        if request.is_authenticated and request.is_blocked_by_admin:
            logout(request)

            return redirect ('blocked')
        response = self.get_response(request)
        return response
        

# ----------------------------------------------------------------------------------------

# MERGE sorted

def merge_sort(arr):
    if len(arr) > 1:
        mid  = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0 
        while i < len(left_arr) and j < len(right_arr) :
            if left_arr[i] <  right_arr[j]:
                arr[ k ] = left_arr[i]
                i += 1
                k +=1 
            else:
                arr[ k] =  right_arr[j]
                j += 1
                k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[ j]
            j += 1
            k += 1


list1 = [1,3,8,5,43,2,3,5,6,89,4,2]


merge_sort(list1)

print(list1)


# ----------------------------------------------------------------------------------------


d = {"a": 5, "b": 2, "c": 9, "d": 1}


tt = dict(sorted(d.items(), key = lambda varr:varr[1] ))
print(tt)



# ----------------------------------------------------------------------------------------

# longest word in string 


s = "my  is fazzzaall  name "

c = s.split()
res = []
maxx = 0
for i in c:
    w = len(i)
    if maxx < w:
        maxx = w
        res = i

print(res)

# -------------------------------------RIYAS---------------------------------------------
arr = [3,38,35,12,41,3,4,23,45,12]

#out: [ 38, 41, 41, 41, 45, 4, 23, 45, -1, -1]

print(len(arr))
res = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] < arr[j]:
            res.append(arr[j])
            break
    if arr[i] > arr[j] or i == len(arr)-1:
        res.append(-1) 

print(res)



# ---------------------------------------GR--------------------------------------------------\\







import requests

print(requests.get('https://jsonplaceholder.typicode.com/todos/1').json())


# ------------------------------------------------------------------------------------
s = "aabbbbbcaaaaaiiiaaaa"
# OUT = "a2b2c1a2"

res = ""
count = 1
for j in range(len(s)-1):
    if len(s)-1 == j+1:
        count += 1
        res += s[j] + str(count)
        break
    if s[j] == s[j+1]:
        count += 1

    else:
        res += s[j] + str(count)
        count=1
        
            
print(res)
        
            