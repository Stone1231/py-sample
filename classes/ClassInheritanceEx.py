from ClassEx import Dog

class SARDog(Dog): 
    """Represent a search dog.""" 
    def __init__(self, name, heigh, weight): 
        """Initialize the sardog.""" 
        super().__init__(name, heigh, weight) 

    def search(self): 
        """Simulate searching.""" 
        print(self.name + " is searching.") 

    def eat_new(self): 
        self.eat() # 不同名才能直接call

    def eat(self): 
        #self.eat() error, 同名不能直接call,免得造成無窮迴圈
        super().eat()
        print("and ZZzzzzz")

        # """Simulate sitting.""" 
        # print(self.persion.name + "'s " + self.name + " is eating.")         
              

my_sardog = SARDog('Willie',220 ,10) 
print(my_sardog.name + " is a search dog.") 
my_sardog.sit() 
my_sardog.search()
my_sardog.eat()
my_sardog.eat_new()



