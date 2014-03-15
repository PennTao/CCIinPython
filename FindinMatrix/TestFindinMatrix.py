import unittest
from FindinMatrix import *

class TestFindinMatrix(unittest.TestCase):
    def test_FindElement(self):
        fem = FindEleinMatrix()
        mat1 = []
        mat2 = [[1,2,3],[2,3,4]]
        mat3 = [[1,2,3],[4,5,6],[7,8,9]]
        mat4 = [[1,2,3]]
        mat5 = [[1,1,1]]

        self.assertEqual(None, fem.FindElement(mat1,2,1,1,1,1))
        self.assertEqual([1,2], fem.FindElement(mat2,4,0,1,0,2))
        self.assertEqual([1,1], fem.FindElement(mat2,3,0,1,0,2))
        self.assertEqual([0,1], fem.FindElement(mat3,2,0,2,0,2))
        self.assertEqual([0,1], fem.FindElement(mat4,2,0,0,0,2))
        
if __name__ == '__main__':
    unittest.main()
