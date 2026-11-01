class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s=set()
        L=sorted(nums)
        c=0
        t=[]
        dicts=defaultdict(list)
        for i in nums :
            s.add(i)
        if k > len(s): return False 
        else :
            for i in s :
                for j in range (0,len(L)) :
                    if L[j]==i :
                        c+=1
                dicts[i].append(c)
            for i in range (0,len(dicts)):
                t.append(dicts[len(dicts)-k].keys())
            return t






        