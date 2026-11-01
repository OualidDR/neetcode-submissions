class Solution:


    def encode(self, strs: List[str]) -> str:
        s=[]
        for i in strs:
           s.append(f'{len(i)}#{i}')
        print("".join(s)) 

    def decode(self, s: str) -> List[str]:
        pass
        

