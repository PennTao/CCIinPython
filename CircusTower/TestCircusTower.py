import unittest
from CircusTower import *

class TestCircusTower(unittest.TestCase):
    def test_BuildLargestTower(self):
        people1 =[(65,170)]
        people2 = []
        people3 = [(65,170),(66,171)]
        people4 = [(70,180),(55,160),(50,159),(65,170),(60,169)]
        people5 = [(66,171),(66,171),(66,171)]
        people6 = [(66,171),(65,170),(50,180),(55,189),(56,190)]
        ct = CircusTower()
        self.assertEqual([(65,170)], ct.BuildLargestTower(people1))
        self.assertEqual([], ct.BuildLargestTower(people2))
        self.assertEqual([(65,170),(66,171)], ct.BuildLargestTower(people3))
        self.assertEqual([(50,159),(55,160),(60,169),(65,170),(70,180)], ct.BuildLargestTower(people4))
        self.assertEqual([(66,171)], ct.BuildLargestTower(people5))
        self.assertEqual([(50,180),(55,189),(56,190)],ct.BuildLargestTower(people6))
if __name__ == '__main__':
    unittest.main()

        
