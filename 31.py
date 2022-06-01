range1 = input("輸入陣列大小：").split(" ")
a = []
b = []
h = int(range1[0])
w = int(range1[1])

for i in range(h):
    a += (input("").split(" "))

for i in range(h):
    b += input("").split(" ")

for i in range(h):
    for j in range(w):
        print(int(a[(h*i)+j])*int(b[(h*i)+j]),end=" ")
    print("")
