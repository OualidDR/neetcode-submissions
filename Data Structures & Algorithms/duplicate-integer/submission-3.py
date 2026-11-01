class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        liste=set()
        for i in nums :
            if i in liste :
                return True 
            else :
                liste.add(i)
        