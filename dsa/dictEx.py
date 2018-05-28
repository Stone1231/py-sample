#A simple dictionary 
alien = {'color': 'green', 'points': 5} 

#同上
alien = {} #an empty dictionary
alien['color'] = 'red' 
alien['points'] = 6

#Accessing a value 
def accessing_ex():
    print("====accessing value====")
    print("The alien's color is " + alien['color']) 
accessing_ex()

def add_del_ex():
    print("====add_del====")
    alien['x_position'] = 0 #Adding a new key-value pair 
    del alien['x_position'] #del
    for item in alien.items(): 
        print(item) 
add_del_ex()

fav_numbers = {'eric': 17, 'ever': 4} 
def looping_items_ex():
    print("====looping items====")
    #Looping through all key-value pairs 
    for name, number in fav_numbers.items(): 
        print(name + ' loves ' + str(number)) 

    #Looping through all keys 
    for name in fav_numbers.keys(): 
        print(name + ' loves a favorite ' + str(fav_numbers[name])) 
        #print(fav_numbers[name])

    #Looping through all the values 
    for number in fav_numbers.values(): 
        print(str(number) + ' is a favorite')  
looping_items_ex()

#sort
def sort_ex():
    print("====sort====")
    sortedNumbers = sorted(fav_numbers.values())
    for number in sortedNumbers: 
        print(number)
sort_ex()

#sort desc
def sort_desc_ex():
    print("====sort desc====")
    sortDescNumbers = sorted(
        fav_numbers.values(), 
        key=lambda x:x, 
        reverse=True)
    for number in sortDescNumbers: 
        print(number)
sort_desc_ex() 

def dict_init():
    print("====dict_init====")
    dict_info = dict(code=0, message="hello")
    print(dict_info)
dict_init()    

def merging():
    print("====merging====")
    fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
    dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
    fishdog = {**fish, **dog}
    print(fishdog) 
    #duplicate keys map to their lattermost value
    #更新最新值
merging()    