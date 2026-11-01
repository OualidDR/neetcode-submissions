class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums :
            return 0
        if len(nums) == 1 :
            return 1 
        x = 0
        count = 1
        L = sorted(nums)
        s = set()
        for i in L:
            s.add(i)
        N = sorted(list(s)) #[2,3,4,5,10,20]
        for i in range(len(N)-1) :
            if N[i+1] == N[i] + 1 :
                count +=1
            else:
                count = 1
            x = max(x, count)
        return x
        

        
        