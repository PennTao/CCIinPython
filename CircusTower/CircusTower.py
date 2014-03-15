#A circus is designing a tower routine consisting of people standing atop one another's shoulder
#For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her.
#Given the heights and weights of each person in the circus, write a method to compute
#the largest possible number of people in such a tower

class CircusTower(self):
    def BuildLargestTower(self, people):
        if (len(people) == 0 or people == None):
            return []

