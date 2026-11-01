class Solution:


    def encode(self, strs: List[str]) -> str:
        s=[]
        for i in strs:
           s.append(f'{len(i)}#{i}')
        return "".join(s)

    def decode(self, s: str) -> List[str]:
        pass
        

