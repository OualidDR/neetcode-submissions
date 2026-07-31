class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a= sorted(s)
        x = "".join(a)
        b= sorted(t)
        y = "".join(b)
        if x == y : 
            return True
        return False

