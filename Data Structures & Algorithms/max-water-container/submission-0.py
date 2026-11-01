class Solution:
    def maxArea(self, H: List[int]) -> int:
        maxarea = 0
        for i in range(len(H)-1):
            for j in range(i+1, len(H)):
                if (j-i) * min(H[i],H[j]) > maxarea :
                    maxarea = (j-i) * min(H[i],H[j])
        return maxarea


        