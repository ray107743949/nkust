all = set(["John","Mary","Tina","Fiona","Claire","Eva","Ben","Bill","Bert"])
english_pass = set(["John","Mary","Fiona","Claire","Ben","Bill"])
math_pass = set(["Mary","Fiona","Claire","Eva","Ben"])
print("英文跟數學都及格：",english_pass.intersection(math_pass))#交集
print("數學不及格：",all.difference(math_pass))#差集
print("英文跟數學都不及格：",(all.difference(math_pass).intersection(english_pass)))