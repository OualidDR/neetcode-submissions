class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        else :
            for i in t :
                if i not in  s :
                    return False
            return True
        