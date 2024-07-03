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

        # ----------------------------------------------------------------------------------------
    
    
    

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



s = "xoxyyoyydfgwdfopkpofdf"

count = 0

def is_palindrom(arr):
    return arr == arr[::-1]

for i in range(len(s)-2):
    for j in range(i+3, len(s)+1):
        if is_palindrom(s[i:j]):
            count += 1
      

print(count)
        
# ----------------------------------------------------------------------------------------

d = {"a": 5, "b": 2, "c": 9, "d": 1}


tt = dict(sorted(d.items(), key = lambda varr:varr[1] ))
print(tt)
