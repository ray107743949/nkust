import re
str1 = input("：")
str1 = re.sub("[a,e,i,o,u]",".",str1)
print(str1)

