class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [1, 2, 3, 5, 9, 4]
        nums.sort()
        # [1, 2, 3, 4, 5, 9]
        count = 1
        Max = 1
        if nums == [] :
            return 0
        for i in range(len(nums)-1) :
            if nums[i+1] == nums[i] + 1  :
                count += 1
                if count > Max :
                    Max = count 
            elif nums[i+1] != nums[i] :
                count = 1

        return Max



        