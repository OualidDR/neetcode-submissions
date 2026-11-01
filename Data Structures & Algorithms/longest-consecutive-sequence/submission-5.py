class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        [2,3,4,5,10,20]
        maxe = 0
        count = 2
        L = sorted(nums)
        s = set()
        for i in L:
            s.add(i)
            N = list(s)
        for i in range(len(N)-1) :
            if N[i+1] > N[i] + 1 :
                count +=1
            else :
                count = 1 
        if count > maxe :
            maxe = count
        return maxe 
        

        
        