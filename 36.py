time = int(input("幾筆資料："))
list = []
for i in range(time):
    for j in range(4):
       list.append(int(input("")))
    if list[0]/list[1] == list[2]/list[3]:
        for j in range(4):
            print(list[j],end=" ")
        print(list[3]/(list[0]/list[1]))
        print("為等比數列")
    elif list[0]-list[1] == list[2]-list[3]:
        for j in range(4):
            print(list[j],end=" ")
        print(list[3] - (list[2]-list[3]))
        print("為等差數列")
    list.clear()

