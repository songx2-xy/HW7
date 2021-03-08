import unittest
from FizzBuzz import*
class TestCase(unittest.TestCase):
    def test_FizzBuzz1(self):
        self.assertEqual(FizzBuzz(1), 1)
if __name__=='__main__':
    unittest.main()
    