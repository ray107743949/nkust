n = int(input("輸入："))
print("數列：%d"%n,end=" ")
while not(n == 1):
    if n%2 == 1:
        n = int(n*3 + 1)
    else:
        n = int(n/2)
    print(n,end=" ")





