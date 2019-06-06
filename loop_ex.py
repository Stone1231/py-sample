for i in [0, 1, 2, 3, 4]:
    print(i)

for i in range(5):
    print(i)

for x in range(1, 6):
    print(x)

for i in range(3):
    print(i)
else:
    print('done')

#A simple while loop 
current_value = 1 
while current_value <= 5: 
    print(current_value) 
    current_value += 1 

#Letting the user choose when to quit 
msg = '' 
while msg != 'quit': 
    msg = input("What's your message? ") 
    print(msg)
