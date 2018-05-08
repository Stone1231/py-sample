from ClassEx import Dog

class SARDog(Dog): 
    """Represent a search dog.""" 
    def __init__(self, name, heigh, weight): 
        """Initialize the sardog.""" 
        super().__init__(name, heigh, weight) 

    def search(self): 
        """Simulate searching.""" 
        print(self.name + " is searching.") 

my_sardog = SARDog('Willie',220 ,10) 
print(my_sardog.name + " is a search dog.") 
my_sardog.sit() 
my_sardog.search()


