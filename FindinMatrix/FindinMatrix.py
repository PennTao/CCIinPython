#11.6 Given M by N matrix in which each row and each column is sorted in ascending order,
#write a method to find an element
class FindEleinMatrix:
    def FindElement(self, mat, ele, mbegin,mend,nbegin,nend):
        if(len(mat) == 0):
            return None
        if(mbegin < 0 or nbegin < 0):
            return None
        if(mend >= len(mat) or nend >= len(mat[0])):
            return None
        if(mbegin > mend or nbegin > nend):
            return None
        mmid = (mbegin + mend)/2
        nmid = (nbegin + nend)/2
        if( ele > mat[mmid][nmid]):
            if(mmid + 1 < len(mat)):
                mmid = mmid + 1
            if(nmid + 1 < len(mat[0])):
                nmid = nmid + 1         
            return self.FindElement(mat,ele,mmid, mend, nmid,nend)
        elif(ele < mat[mmid][nmid]):
            for i in range(0,nmid):
                if(ele == mat[mmid][i] ):
                    return [mmid,i]
            for i in range(0,mmid):
                if(ele == mat[i][nmid]):
                    return [i,nmid]
            if(mmid - 1 >= 0):
                mmid = mmid - 1
            if(nmid - 1 >= 0):
                nmid = nmid - 1
            return self.FindElement(mat,ele,mbegin,mmid ,nbegin,nmid )
        
        elif( ele == mat[mmid][nmid]):
            return [mmid,nmid]

            
