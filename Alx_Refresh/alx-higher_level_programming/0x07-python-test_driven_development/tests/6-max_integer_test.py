import unittest

max_integer = __import__('6-max_integer.py').max_integer

class TestMaxInteger(unittest.TestCase):
    """To test the max integer function"""
    def test_max_integer(self):
         #Test the max integer of a list input
         self.assertEqual(max_integer([]), None)
         self.assertEqual(max_integer([2,1]), 2)
         self.assertEqual(max_integer([1,4,5,1,4,9]), 9)
    def test_empty_list(self):
         """Test empty list"""
         self.assertEqual(max_integer([]), None)
    def test_string(self):
         list = ['4', '5', 'f']
         self.assertEqual(max_integer([list]), 'must be a list of integers')

if __name__ == '__main__':
     unittest.main()