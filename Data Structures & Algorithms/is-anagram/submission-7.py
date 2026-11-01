class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        else :
            for i in t :
                if i  in  s :
                    if count(t(i))!=count(s(j)):
                        return False 
                    
            return True
        