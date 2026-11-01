class Solution:

    def encode(self, strs: List[str]) -> str:
        L= []
        for i in strs :
            L.append(str(len(i))+'#'+i)
        return L

    def decode(self, s: str) -> List[str]:
        return s 
        
