number = int(input(""))

for i in range(1,number,2):
    print(" "*(number//2)+str(i))

for i in range(1,number+1,2):
    print(i,end="")
for i in range(number-2,0,-2):
    print(i,end="")
print("")
for i in range(number-2,0,-2):
    print(" "*(number//2)+str(i))