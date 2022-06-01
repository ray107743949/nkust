n = int(input(":"))


for i in range(1,n+1):
    now = 0
    for j in range(i):
        now += i
        print(now,end=" ")
    print()
