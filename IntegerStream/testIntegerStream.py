import unittest
from IntegerStream import *

class TestIntegerStream(unittest.TestCase):
    def test_getRank(self):
        data = IntegerStream()
        self.assertEqual(-1,data.getRankOfNumber(1))
        data.track(1)
        self.assertEqual(0,data.getRankOfNumber(1))
        data.track(1)
        self.assertEqual(1,data.getRankOfNumber(1))
        data.track(2)
        self.assertEqual(-1,data.getRankOfNumber(7))
        self.assertEqual(1,data.getRankOfNumber(1))
        self.assertEqual(2,data.getRankOfNumber(2))
        data.track(2)
        self.assertEqual(3,data.getRankOfNumber(2))
        self.assertEqual(-1,data.getRankOfNumber(20))
if __name__ == '__main__':
    unittest.main()
