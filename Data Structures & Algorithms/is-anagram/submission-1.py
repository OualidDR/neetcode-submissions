class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s :
            if i not in t and len(t)==len(s): 
                return False 
        return True 
        