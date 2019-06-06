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