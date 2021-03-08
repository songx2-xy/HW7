import unittest
from Year import*
class TestCase(unittest.TestCase):
    def test_Year1(self):
        self.assertEqual(Year(2002), "Not Leap Year")
        self.assertEqual(Year(2021), "Not Leap Year")
        self.assertEqual(Year(1999), "Not Leap Year")
    def test_Year2(self):
        self.assertEqual(Year(2000), "Leap Year")
        self.assertEqual(Year(1600), "Leap Year")
if __name__=='__main__':
    unittest.main()