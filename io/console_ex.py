import sys

name = input("What's your name? ") 
print("Hello, " + name + "!")

age = input("How old are you? ") 
age = int(age)
if age < 4: 
    print('< 4') 
elif age < 18: 
    print('4 ~ 18') 
else: 
    print('18 < ') 