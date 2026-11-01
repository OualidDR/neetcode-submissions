class Solution:

    def encode(self, strs: List[str]) -> str:
        L= []
        for i in strs :
            L.append(str(len(i))+'#'+i)
            sol = "".join(L)
        return sol

    def decode(self, s: str) -> List[str]:
        # L = []
        # start = 2
        # end = int(s[0])+2
        # for i in s:
        #     if end+10 <= len(s) :
        #         s = "".join(s[start:end])
        #         L.append(s)
        #         start = end+3
        #         end += int(s[0]) + 2 
        return s

        

