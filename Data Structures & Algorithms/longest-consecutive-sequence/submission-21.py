
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = sorted(set(nums))
        count = 1
        max_len = 1
        for i in range(len(N) - 1):
            if N[i+1] == N[i] + 1:
                count += 1
            else:
                count = 1
            max_len = max(max_len, count)
        return max_len   

        
        