class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# making a dict with key value the key is the sorted word and the value are the original words and then we return the values !
       dict = defaultdict(list)
       for string in strs :
        s = sorted(string)
        "".join(s)
        dict[str] = string
        return dict