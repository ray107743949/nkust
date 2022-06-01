time = input("輸入時間：").split(":")
second = int(time[0])*60 + int(time[1])

ice = 0
second -=  45
ice += (second//90)*19
ice -= (second//60)
ice += (second%90)//30*6
print(ice)


