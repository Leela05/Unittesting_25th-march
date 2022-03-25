import unittest

def mylist():
    list = [1,2,3,4,5]
    return list

class membershipoperator(unittest.TestCase):
    def test_case1(self):
        item = 23
        self.assertNotIn(item, mylist())

    def test_case2(self):
        item = 4
        self.assertIn(item, mylist())

if __name__ == "__main__":
    unittest.main()