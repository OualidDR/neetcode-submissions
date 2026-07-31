class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c=0
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    c+=1
                    break
            if c!=0:
                break
        if c!=0 :
            return True 
        else :
            return False 
        