import unittest
from StringFinder import *

class TestStringFinder(unittest.TestCase):
    def test_FindString(self):
        sf = StringFinder()
        strList1 = []
        strList2 = ["at","","","","ball","","","car","","","dad","",""]
        strList3 = ["at","","","",""]
        strList4 = ["","","","at"]
        strList5 = ["","","","at",""]
        strList6 = ["","at","","",""]

        self.assertEqual(None,sf.FindString(strList1,"ball",0,1))
        self.assertEqual(4,sf.FindString(strList2,"ball",0,12))
        self.assertEqual(10,sf.FindString(strList2,"dad",0,12))
        self.assertEqual(0,sf.FindString(strList3,"at",0,4))
        self.assertEqual(3,sf.FindString(strList4,"at",0,3))
        self.assertEqual(3,sf.FindString(strList5,"at",0,4))
        self.assertEqual(1,sf.FindString(strList6,"at",0,4))
if __name__ == '__main__':
    unittest.main()
