import unittest
from Leap import*
class TestCase(unittest.TestCase):
    def test_leapyear1(self):
        self.assertEqual(leapyear(2001), "No")
if __name__=='__main__':
    unittest.main()
