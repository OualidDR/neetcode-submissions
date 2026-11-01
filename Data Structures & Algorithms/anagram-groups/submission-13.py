class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c=[]
        l=[]
        x=[]
        for i in range (0,len(strs))  :
            l.append(''.join(sorted(strs[i])))
    
        for i in range(0,len(l)-1):
            if i not in x :
                 x.append(i)
                 c.append(''.join(strs[i]))
            for j in range(i+1,len(l)) :
                if j not in x and l[i]==l[j] :
                    list(c[i]).append(strs[j])
                
        return  l