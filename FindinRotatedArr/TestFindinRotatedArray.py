import unittest
from FindinRotatedArray import * 

class TestFindinRotatedArray(unittest.TestCase):   
    def setUp(self):
        self.arr1 = [2]
        self.n1 = 2
        self.arr2 = [5,6,7,3,4]
        self.n21 = 7
        self.n22 = 3
        self.arr3 = []
        self.arr4 = [6,7,8,9,1,2,3]
        self.n4 = 5
        self.arr5 = [2,2,2,3,4,2]
        self.arr6 = [2,3,4,2,2,2]

        self.cls = FindinRotatedArray()
        pass
    def test_Find(self):
        self.assertEqual(0, self.cls.Find(self.arr1,self.n1,0,1))
        self.assertEqual(2,self.cls.Find(self.arr2,self.n21,0,4))
        self.assertEqual(3,self.cls.Find(self.arr2,self.n22,0,4))
        self.assertIsNone(self.cls.Find(self.arr3,1,0,0))
        self.assertEqual(None, self.cls.Find(self.arr4,self.n4,0,6))
        self.assertEqual(3,self.cls.Find(self.arr5,3,0,5))
        self.assertEqual(1,self.cls.Find(self.arr6,3,0,5))
if __name__ == '__main__':
    unittest.main()
