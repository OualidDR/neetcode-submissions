class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        L= []
        for i in strs :
            L.appen("".join(sorted(i)))
        return L
