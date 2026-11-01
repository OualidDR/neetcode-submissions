class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c=[]
        l=[]
        for i in range (0,len(strs)) :
            l.append(sorted(strs[i]))
    
        for i in range(0,len(l)-1):
            for j in range(i+1,len(l)):
                c.append(strs[i])
                if l[i]==l[j]:
                    c[i].append(strs[j])
        return c 
        
                    


        