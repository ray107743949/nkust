n = int(input("輸入有幾個點："))
list1 = []
count = 0
for i in range(n):
    number = int(input("輸入第"+str(i+1)+"個："))
    if number % 11 == 0 or number % 9 == 0:
        count += 1
        list1.append("第"+str(i+1)+"個點"+str(number))
if count == 1:
    print("0")
else:
    for i in list1:
        print(i)
