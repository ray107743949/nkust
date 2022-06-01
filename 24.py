time =  int(input("n*n請輸入n："))

list = []
maxlist = []
index = []
total = 0

for i in range(time):
    x = input("").split(" ")
    for j in x:
        list.append(int(j))

for i in range(3):
    y = int(max(list))
    maxlist.append(y)
    index.append([(int(list.index(y))+i)//time+1,(int(list.index(y)+i))%time+1])
    list.remove(y)
    total += y

print(total)
print(index)



