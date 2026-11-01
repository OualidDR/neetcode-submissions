# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         L= []
#         for i in range(len(nums)):
#             prod = 1
#             for j in range(len(nums)):
#                 if i !=j:
#                     prod *= nums[j]
#             L.insert(i, prod)
            
#         return L

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]

            res[i] = prod
        return res

                

        