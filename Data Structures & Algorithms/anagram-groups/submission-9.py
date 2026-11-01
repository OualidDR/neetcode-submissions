class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c=[]
        l=[]
        for i in range (0,len(strs)) :
            l.append(''.join(sorted(strs[i])))
    
        for i in range(0,len(l)-1):
            for j in range(i+1,len(l)):
                c.append(''.join(strs[i]))
                if l[i]==l[j]:
                    list(c[i]).append(strs[j])
        return c