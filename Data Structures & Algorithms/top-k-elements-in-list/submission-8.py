class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        L=[]
        count=Counter(nums)
        sorted_dict=sorted(count.items(),key= lambda x:x[1])
        for i in range(len(sorted_dict),len(sorted_dict)-k,-1):
            L.append(sorted_dict[i].values())
        return(L)
        





        