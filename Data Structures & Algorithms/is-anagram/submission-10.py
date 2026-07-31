class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s) :
            return False
 
        else :
            S=sorted(s)
            T=sorted(t)
            for i in range(0,len(T)) : 
                if T[i]!=S[i]:
                    return False 
        return True 

        