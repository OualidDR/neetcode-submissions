class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        sorted_dict=dict(sorted(count.items(),key= lambda x:x[1], reverse = True))
        return [i[0] for i in sorted_dict[:k] ]


        
        





        