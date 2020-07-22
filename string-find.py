s = "That I ever did see. Dusty as the handle on the door"

index = s.find("Dusty")
print(index)

s = "That I ever did see. Dusty as the handle on the door"

if "Dusty" in s:
    print("query found")

"""
Exercise
Try the exercises below

1.Find out if string find is case sensitive
2.What if a query string appers twice in the string?
3.Write a program that asks console input and searches for a query.
"""

#Find out if string find is case sensitive
s = "THAT I EVER DID SEE. DUSTY AS THE HANDLE ON THE DOOR"

if "Dusty" in s:
    print("query found")
else:
    print("query not found")   

#What if a query string appers twice in the string?
s = "Hello world world"

index = s.find("world")
print(index)

#Write a program that asks console input and searches for a query.
s = input("请输入字符串：")
p = input("请输入要查找的字符串：")
if p in s:
    print("查找成功")
else:
    print("查找失败")
    
