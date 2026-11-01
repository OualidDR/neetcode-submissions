class Solution:
    def isValid(self, s: str) -> bool:
        s = "([{}])"
        n = len(s)
        dict = {1:['[', ']'], 2:['{', '}'], 3:['(', ')']}
        for i in range(int(n/2)+1) :
            for key in dict:
                if s[i] in key.values() & s[n-i] in key.values() :
                    continue
                else : 
                    return False 
        return True 

        