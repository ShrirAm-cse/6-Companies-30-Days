# problem link - https://leetcode.com/problems/combination-sum-iii/description/

class Solution:
    def rsum(self,k,n,res,csum,ind,temp):
        if csum==n and len(temp)==k:
            t=[x for x in temp]
            res.append(t)
            return
        if ind==10 or len(temp)==k:
            return 
        if csum>n:
            return
        if csum==n and len(temp)<k:
            return 
        
            
        self.rsum(k,n,res,csum,ind+1,temp)
        csum+=ind
        temp.append(ind)
        self.rsum(k,n,res,csum,ind+1,temp)
        temp.pop(-1)
        return


    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        self.rsum(k,n,res,0,1,[])
        return res