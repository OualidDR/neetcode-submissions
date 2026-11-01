class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        L=[]
        count=Counter(nums)
        sorted_dict=dict(sorted(count.items(),key= lambda x:x[1], reverse = True))
        return [i.values() for i in sorted_dict.items() ]


        
        





        