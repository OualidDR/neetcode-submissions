class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c=[]
        l=[]
        x=[]
        for i in range (0,len(strs))  :
            l.append(''.join(sorted(strs[i])))
    
        for i in range(0,len(strs)-1):
            if i not in x :
                 x.append(i)
                 c.append(strs[i])
            for j in range(i+1,len(strs)) :
                if j not in x and l[i]==l[j] :
                    c[i].append(strs[j])
                
        if len(strs)-1 not in x :
            c.append(strs[len(strs)-1])
        return c