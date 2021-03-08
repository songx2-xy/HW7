import unittest
from Year import*
class TestCase(unittest.TestCase):
    def test_Year1(self):
        self.assertEqual(Year(2002), "No")
if __name__=='__main__':
    unittest.main()