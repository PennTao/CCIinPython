#A circus is designing a tower routine consisting of people standing atop one another's shoulder
#For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her.
#Given the heights and weights of each person in the circus, write a method to compute
#the largest possible number of people in such a tower
import copy

class CircusTower:
    def BuildLargestTowerHelper(self, people,person, mRec):
        if (len(people) == 0 or people == None or person == None):
            return
        if(person in mRec):
            return mRec[person]
        maxCount = 0
        maxTower = []                
        for curP in people:
            if curP[0] < person[0] and curP[1] < person[1]:
                curTower = self.BuildLargestTowerHelper(people,curP,mRec)
                if curTower != None:
                    if len(curTower) > maxCount:
                        #maxTower = copy.deepcopy(curTower)
                        #maxTower = copy.copy(curTower)
                        maxTower = curTower
                        maxCount = len(curTower)
        res = [person]
        mRec[person] = maxTower + res
        return mRec[person]

    def BuildLargestTower(self,people):
        maxCount = 0
        maxTower = []
        mRec = dict()
        for person in people:
            curTower = self.BuildLargestTowerHelper(people,person , mRec)
            if curTower != None:
                if len(curTower) > maxCount:
                    maxCount = len(curTower)
                    maxTower = curTower
        
        return maxTower
