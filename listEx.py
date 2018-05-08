from time import sleep

bikes = ['trek', 'redline', 'giant']

def get_first_last_ex():    
    first_bike = bikes[0] #Get the first item in a list
    last_bike = bikes[-1] #Get the last item in a list
    print("====get_first_last====")
    print(first_bike)
    print(last_bike)
get_first_last_ex()

def append_insert_ex():  
    bikes.append('giant') #塞入一筆
    bikes.insert(0,'stone') #從index塞入
    print("====append_insert====")
    for bike in bikes: 
        print(bike)
append_insert_ex()

def count_len_ex():  
    print("====count_len====")
    print(bikes.count('giant')) #出現兩次 
    print(len(bikes)) #取得總筆數
count_len_ex()

def remove_ex():  
    print("====remove====")
    bikes.remove('giant') #兩個giant,只會移掉一筆
    del bikes[0]
    for bike in bikes: 
        print(bike)
remove_ex()

def pop_ex():
    print("====Pop the last item from a list====")
    #Pop the last item from a list
    most_recent_bike = bikes.pop() 
    print("pop's item is " + most_recent_bike)
    for bike in bikes: 
        print(bike)
pop_ex()

def indexof_ex():
    print("====indexof====")
    print("trek's index is " + str(bikes.index("trek")))
indexof_ex()

def upper_and_deltop2_ex():
    print("====upper and deltop2====")
    upper_bikes = [bike.upper() for bike in bikes]
    for bike in upper_bikes: 
        print(bike)
    del upper_bikes[:2] #刪掉前2筆        
upper_and_deltop2_ex()        

def square2_range_ex():
    #Making numerical lists 
    print("====square2 range====")
    squares = [] 
    for x in range(1, 11): # 1到10,沒有11
        squares.append(x**2)
    for square in squares: 
        print(square)
square2_range_ex()

def square3_range_ex():
    print("====square3 range====")
    """
    List comprehensions 
    """
    squares = [x**3 for x in range(1, 11)] 
    for square in squares: 
        print(square)
square3_range_ex()

def slicing_list_ex():
    print("====Slicing a list====")
    finishers = ['sam', 'bob', 'ada', 'bea'] 
    first_two = finishers[:2] 
    for finisher in first_two:     
        print(finisher)
slicing_list_ex()

def copying_list_ex():
    #Copying a list (不是參考到同個物件)
    print("====Copying a list====")
    copy_of_bikes = bikes[:] #跟copy_of_bikes = bikes 一樣

    for bike in copy_of_bikes: 
        bike = bike + '_x' #只是取值而已,不會影響到成員的值

    for i, bike in enumerate(copy_of_bikes):
        copy_of_bikes[i] = copy_of_bikes[i] + '_copy'     

    for bike in copy_of_bikes:     
        print(bike)
copying_list_ex()

def check_item_ex():
    print("====check item====")
    print('trek' in bikes)
    print('trek' not in bikes)
    print('surly' not in bikes)
    print(bikes[0] == 'trek')
check_item_ex()
