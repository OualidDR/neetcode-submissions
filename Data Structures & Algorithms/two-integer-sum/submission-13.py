class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L=[]
        c = []
        for i in nums :
            if i <= target :
                L.append(i)
        if len(L) == 0 :
            print("no combinison")
        for i in range(0, len(L)-1):
            for j in range(1, len(L)) :
                if (L[i]+L[j]) == target :
                    c.append(i)
                    

        return c


 