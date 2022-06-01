from itertools import count
import re
str1 = re.split(",|。",input("："))
str2 = ""
list1 = []
for i in str1:
    str2 += i
for i in str2:
    if str.count(i) > 1 :        
        list1.append(i)

print(set(list1))

 