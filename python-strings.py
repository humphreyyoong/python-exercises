from datetime import date
x = "Hello"
print(x)

print(x[0])
print(x[1])

x = "hello world"
s = x[0:3]
print(s)
s = x[:3]
print(s)

x = "Nancy"
print(x)

s = "My lucky number is %d, what is yours?" % 7
print(s)

s = "My lucky number is " + str(7) + ",what is yours?"
print(s)

print(x[0])

print(x[0:3])

"""
Exercises
Try the exercises below

Make a program that displays your favourite actor/actress.
Try to print the word ‘lucky’ inside s.
Try to print the day, month, year in the form “Today is 2/2/2016”.

"""

actor = "lixiaolai"
print(actor)
print(s[3:7])
d = date.today()
formatdate = d.strftime("%m/%d/%Y")
print("Today is " + formatdate)

