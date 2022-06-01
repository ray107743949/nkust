n = input("輸入比數：")
medal = {}
for i in range(int(n)):
    x = input("：").split(" ")
    medal[x[0]] = x[1]
for i in medal:
    print(i,medal[i])
