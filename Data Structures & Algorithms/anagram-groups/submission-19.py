class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        L= []
        for i in strs :
            L.append(sorted(i))
        return L