import heapq 
nums = []
for i in range(1,11):
    nums.append(int(input("第"+str(i)+"個:")))   
print(heapq.nlargest(3,nums)) 
print(heapq.nsmallest(3,nums)) 