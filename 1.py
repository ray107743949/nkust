num = input("輸入正整數:")
list_num = []
biggest = 0
nn = 0
TorF = False
for i in range(0,len(num)):
    for j in range(0,len(num)):
        list_num.append(num[i:j+1])
# print(list_num)
while('' in list_num):
    list_num.remove('')
while(num in list_num):
    list_num.remove(num)

print(list_num)


for i in list_num:
    a = int(i)
    for j in range(2,a):
        print(j)
        TorF = False
        if a % j == 0:
            TorF = False
            break
        else:
            TorF = True

        if TorF == True and a > biggest:
            biggest = a
            print(biggest)

if biggest == 0:
    print("No prime found")
else:
    print("子字串中最大的質數值為:" + str(biggest))