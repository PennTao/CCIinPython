#Give a sorted array of n integers that has been rotated an unknown number of times,
#write code to find an element in the array
class FindinRotatedArray:
    def Find(self,array,n,left,right):
        if(array ==[] or array == None):
            return None
        mid = (left + right)/2
        if(array[mid] == n):
            return mid
        if(left > right):
            return None

        if(array[mid] < array[right]):
            if(n >= array[mid] and n <= array[right]):
                return self.Find(array,n,mid+1,right)
            else:
                return self.Find(array,n,left,mid-1)
        elif(array[mid] > array[left]):
            if(n>=array[left] and n <= array[mid]):
                return self.Find(array,n,left,mid-1)
            else:
                return self.Find(array,n,mid+1,right)
        elif(array[mid] == array[left]):
            if(array[right]!=array[mid]):
                return self.Find(array,n,mid+1,right)
            else:
                res = self.Find(array,n,left,mid-1)
                if(res == None):
                    return self.Find(array,n,mid+1,right)
                else:
                    return res

