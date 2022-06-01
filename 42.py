print("aX^2 + bX + c ")
list1 = input("輸入(a,b,c)：").split(" ")
a = int(list1[0])
b = int(list1[1])
c = int(list1[2])

d = (b*b-4*a*c)**0.5
x1 = (-b+d)/2*a
x2 = (-b-d)/2*a

print(x1,x2)
