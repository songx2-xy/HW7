import unittest
from FizzBuzz import*
class TestCase(unittest.TestCase):
    def test_FizzBuzz1(self):
        self.assertEqual(FizzBuzz(1), 1)
        self.assertEqual(FizzBuzz(2), 2)
        self.assertEqual(FizzBuzz(7), 7)
    def test_FizzBuzz2(self):
        self.assertEqual(FizzBuzz(3), "Fizz")
        self.assertEqual(FizzBuzz(6), "Fizz")
        self.assertEqual(FizzBuzz(9), "Fizz")
if __name__=='__main__':
    unittest.main()
    