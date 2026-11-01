class Solution:

    def encode(self, strs: List[str]) -> str:
        L= []
        for i in strs :
            L.append(str(len(i))+'#'+i)
            s = "".join(L)
        return s

    def decode(self, s: str) -> List[str]:
        pass
