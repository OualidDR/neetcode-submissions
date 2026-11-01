class Solution:

    def encode(self, strs: List[str]) -> str:
        L= []
        for i in strs :
            L.append(str(len(i))+'#'+i)
            s = "".join(L)
        return s

    def decode(self, s: str) -> List[str]:
        L = []
        start = 2
        end = int(s[0])+2
        s = "".join(s[start:end])
        return list(s)

