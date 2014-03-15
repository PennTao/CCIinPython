import uniitest
from CircusTower import *

class TestCircusTower(unittest.TestCase):
    def test_BuildLargestTower(self):
        people1 =[(65,170)]
        people2 = []
        people3 = [(70,180),(55,160),(50,159),(65,170),(60,169)]
        people4 = [(66,171),(66,171),(66,171)]
        blt = BuildLargestTower()
        self.assertEqual([(65,170)], blt.BuildLargestTower(people1))
        self.assertEqual([], blt.BuildLargestTower(people2))
        self.assertEqual([(50,159),(55,160),(60,169),(65,170),(70,180)], blt.BuildLargestTower(people3))
        self.assertEqual([(66,171)], blt.BuildLargestTower(people4))
if __name__ == '__main__':
    unittest.main()

        
