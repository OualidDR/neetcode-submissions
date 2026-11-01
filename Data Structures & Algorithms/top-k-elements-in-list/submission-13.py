class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        L=[]
        i=0
        count=Counter(nums)
        sorted_dict=dict(sorted(count.items(),key= lambda x:x[1]))
        while i < k :
            L.append(sorted_dict(len(sorted_dict)-i-1).keys())
            i+=1
        return(L)
        





        