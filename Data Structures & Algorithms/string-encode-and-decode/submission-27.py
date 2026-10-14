class Solution:

    def encode(self, strs: List[str]) -> str:
        L = []
        for i in strs:
            L.append(str(len(i)) + '#' + i)
        return "".join(L)

    def decode(self, s: str) -> List[str]:
        L = []
        i = 0
        while i < len(s):
            delimiter = s.find('#', i)
            length = int(s[i:delimiter])
            start = delimiter + 1
            end = start + length
            L.append(s[start:end])
            i = end
        return L