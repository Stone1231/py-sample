import unittest

#from unittest import skip


#@skip
class Test_Ex(unittest.TestCase):
    def test_ok(self):
        print("會經過這")
        self.assertEqual(4, 4)

    @unittest.skip
    def test_skip(self):
        print("不會經過這")
        self.assertEqual(3, 4)


# if __name__ == '__main__':
#     unittest.main()

# @unittest.test
# def test_skip2():
#     print("ooxxoox")
#     self.assertEqual(3, 4)