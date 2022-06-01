from array import array


array= []

print("輸入一2*2的矩陣計算其反矩陣")

for i in range(2):
    array += input().split(" ")
array[4-1],array[1-1] = array[1-1],array[4-1]
array[1]="-"+str(array[1])
array[2]="-"+str(array[2])
print("|",array[0],"  ",array[1],"|")
print("|",array[2],"  ",array[3],"|")