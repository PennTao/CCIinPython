#Given a sorted array of strings which is interspersed with empty strings,
# write a method to find the location of a given string
class StringFinder:
    def FindString(self, strList, s,left,right):
        if(strList == [] or strList == None):
            return None
        if(left>right):
            return None
        mid = (left+right)/2
        while( mid <= right and strList[mid] ==""):
            mid = mid +1
        if(mid <=right):
            if(strList[mid] == s):
                return mid
        elif(mid > right):
            mid = (left+right)/2
            while(mid >= left and strList[mid] =="" ):
                mid = mid - 1
            if(strList[mid] == s):
                return mid
        if( s < strList[mid]):
            return self.FindString(strList,s,0,mid-1)
        else:
            return self.FindString(strList,s,mid+1,right)
        
