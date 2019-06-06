import unittest

class Dog(): 
    """Represent a dog.""" 
    def __init__(self, name, heigh, weight): 
        """Initialize dog object.""" 
        self.name = name 
        self.heigh = heigh
        self.weight = weight

class OOPTestCase(unittest.TestCase): 

    def setUp(self): 
        self.dog = Dog('ccc',11,22)

    def test_dog(self): 
        dogName = 'ccc'
        self.assertEqual(dogName, self.dog.name)