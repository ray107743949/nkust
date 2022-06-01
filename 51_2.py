import re
string = input("：")
string = re.sub("\!|\'|\?\,|\。|","",string)
list1 = []
for i in string :
    if str.count(i) > 1 :        
        list1.append(i)

print(set(list1))
