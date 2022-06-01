t = int(input("搭了幾次："))
now = 1
cost = 0 
for i in range(t):
    number = int(input("到幾樓："))
    if number - t > 0:
        cost += 20*(number - t)
    else:
        cost -= 10*(number - t)
    now = number
print(cost)


