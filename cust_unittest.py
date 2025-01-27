import unittest
from app import add, subtract

class TestApp(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
    
    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
    
    def test_something(self):
        subtract(2,1) == 1
        

if __name__ == '__main__':
    unittest.main()
