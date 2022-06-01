x = int(input("："))
total = 0

total += (x//100)
x -= (x//100)*100

total += (x//50)
x -= (x//50)*50

total += (x//10)
x -= (x//10)*10

total += (x//5)
x -= (x//5)*5

total += (x//1)
x -= (x//1)*1

print(total)

