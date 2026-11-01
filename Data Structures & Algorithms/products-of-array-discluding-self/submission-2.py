class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L= [len(nums)]
        prod = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i !=j:
                    prod *= nums[j]
            L.insert(i, prod)
            prod = 1 
        return L[:-1]



                

        