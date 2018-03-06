#Importing individual classes from a module
from dogClass import Dog

my_dog = Dog('Peso',120 ,50) 
print(my_dog.name + " is a great dog!") 
my_dog.sit()

my_dog2 = my_dog #ref obj, 不是copy額外的物件
my_dog2.name = 'ddd'
my_dog.sit()

#Importing an entire module
import dogClass
my_persion = dogClass.Persion('tom')
print("user's name is " + my_persion.name) 

#Importing all classes from a module
from dogClass import *

dogs = [
    Dog('dogA',140, 60), 
    Dog('dogB',140, 40), 
    Dog('dogC',120, 50)]

dogs.append(Dog('dogD',220, 150))

for dog in dogs: 
    print(dog.name)

sortDescLists = sorted(
    dogs, 
    key=lambda x:(x.heigh, x.weight),  # 倒排加負號 ex: -x.weight
    reverse=True)

for dog in sortDescLists: 
    print(dog.name)  