x = int(input("輸入正整數:"))
list1 = []
total = 0
error1 = False
for i in range(1,x):
    if x % i == 0 :
        list1.append(i)
        error1 = True 
print(list1)        
if error1:
    for i in list1 :
        total += i
    if total == x :
        print("pcrfcct")
    elif total > x :
        print("abundant")
    elif total < x:
        print("deficicnt")