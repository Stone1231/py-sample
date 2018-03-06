from time import sleep

bikes = ['trek', 'redline', 'giant']

first_bike = bikes[0] #Get the first item in a list
last_bike = bikes[-1] #Get the last item in a list

print(first_bike)
print(last_bike)

bikes.append('giant') #塞入一筆
bikes.insert(0,'stone') #從index塞入

for bike in bikes: 
    print(bike)

print(bikes.count('giant')) #出現兩次 
print(len(bikes)) #取得總筆數

bikes.remove('giant') #兩個giant,只會移掉一筆
del bikes[0]
for bike in bikes: 
    print(bike)

#Pop the last item from a list
most_recent_bike = bikes.pop() 
print("pop's item is " + most_recent_bike)
for bike in bikes: 
    print(bike)

print("trek's index is " + str(bikes.index("trek")))

upper_bikes = [bike.upper() for bike in bikes]
for bike in upper_bikes: 
    print(bike)

del upper_bikes[:2] #刪掉前2筆

#Making numerical lists 
squares = [] 
for x in range(1, 11): # 1到10,沒有11
    squares.append(x**2)
for square in squares: 
    print(square)

#List comprehensions 
squares = [x**3 for x in range(1, 11)] 
for square in squares: 
    print(square)

#Slicing a list 
finishers = ['sam', 'bob', 'ada', 'bea'] 
first_two = finishers[:2] 
for finisher in first_two:     
    print(finisher)

#Copying a list (不是參考到同個物件)
copy_of_bikes = bikes[:] #跟copy_of_bikes = bikes 一樣

for bike in copy_of_bikes: 
    bike = bike + '_x' #只是取值而已,不會影響到成員的值

for i, bike in enumerate(copy_of_bikes):
    copy_of_bikes[i] = copy_of_bikes[i] + '_copy'     

for bike in copy_of_bikes:     
    print(bike)

print('trek' in bikes)
print('trek' not in bikes)
print('surly' not in bikes)
print(bikes[0] == 'trek')

#Tuples
'''
Tuples are similar to lists, 
but the items in a tuple can't be modified. 
Making a tuple 
'''
dimensions = (1920, 1080)
for dimension in dimensions:
    print(dimension)

for i, dimension in enumerate(dimensions):
    print(i, dimension)    
    #dimensions[i] = dimensions[i] + 100000  不能更新異動

players = [] 
if players: 
    for player in players: 
        print("Player: " + player.title()) 
else: 
    print("We have no players yet!")