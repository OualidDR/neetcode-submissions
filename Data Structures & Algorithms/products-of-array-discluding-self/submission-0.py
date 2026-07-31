class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        t = []
        for i in range(len(nums)):
            # Crée une copie de la liste sans l’élément i
            temp = nums[:i] + nums[i+1:]
            t.append(math.prod(temp))
        return t 
        


        
        