x = input("輸入：")
i = 1
list1 = []
list2 = []
while (x > i):
    i *= 3
    if x < i:
       (i) /= 3
       break
    list1.append(i)
list1 = list(reversed(list1))

while  True :
    list2.append(int(x//i))
    x = x % 3
    i = i//3
    if i == 0:
        break

for i in list2:
    print(i,end="")