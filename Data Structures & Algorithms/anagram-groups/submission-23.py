class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        L= []
        for i in strs :
           a = sorted(i)
           x = "".join(a)
           L.append(x)
        return L