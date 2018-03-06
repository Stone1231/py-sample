import unittest
from functions import get_full_name
from dogClass import Dog

class NamesTest(unittest.TestCase): 

    def setUp(self): 
        self.dog = Dog('ccc',11,22)

    """Tests for names.py.""" 
    def test_first_last(self): 
        """Test names like Janis Joplin.""" 
        full_name = get_full_name('janis', 'joplin') 
        self.assertEqual(full_name, 'Janis Joplin')

    def test_middle(self): 
        """Test names like David Lee Roth.""" 
        full_name = get_full_name('david', 'roth', 'lee') #error參數不對
        self.assertEqual(full_name, 'David Lee Roth')

    def test_dog(self): 
        dogName = 'ccc'
        self.assertEqual(dogName, self.dog.name)

unittest.main()

