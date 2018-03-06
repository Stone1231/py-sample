#A simple dictionary 
alien = {'color': 'green', 'points': 5} 

#同上
alien = {} #an empty dictionary
alien['color'] = 'red' 
alien['points'] = 6

#Accessing a value 
print("The alien's color is " + alien['color']) 


alien['x_position'] = 0 #Adding a new key-value pair 
del alien['x_position'] #del
for item in alien.items(): 
    print(item) 

#Looping through all key-value pairs 
fav_numbers = {'eric': 17, 'ever': 4} 
for name, number in fav_numbers.items(): 
    print(name + ' loves ' + str(number)) 

#Looping through all keys 
for name in fav_numbers.keys(): 
    print(name + ' loves a favorite ' + str(fav_numbers[name])) 
    #print(fav_numbers[name])

#Looping through all the values 
for number in fav_numbers.values(): 
    print(str(number) + ' is a favorite')  

#sort
sortedNumbers = sorted(fav_numbers.values())
for number in sortedNumbers: 
    print(number)

#sort desc
sortDescNumbers = sorted(
    fav_numbers.values(), 
    key=lambda x:x, 
    reverse=True)
for number in sortDescNumbers: 
    print(number)
 