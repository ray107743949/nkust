import re 

string1 = re.sub("\!|\'|\?\,|\。|","",input("1：") )
string2 = re.sub("\!|\'|\?\,|\。|","",input("2：") )
end_list = []

for i in string1:
    if i in string2:
        end_list.append(i)

print(set(end_list))