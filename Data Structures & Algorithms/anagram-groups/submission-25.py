class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# making a dict with key value the key is the sorted word and the value are the original words and then we return the values !
        res = defaultdict(list)
        for s in strs :
            sorteds = "".join(sorted(s))
            res[sorteds].append(s)
        return list(res.values())
        
