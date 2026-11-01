class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=[]
        count=Counter(nums)
        sorted_dict=sorted(count.items(),key= lambda x:x[1])
        l=[i for i in range(len(sorted_dict),len(sorted_dict)-k,-1)]
        return l
        
        





        