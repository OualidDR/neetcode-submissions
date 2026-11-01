class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sort(s) == sort(t)
