class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for c in s :
            if c in pairs and stack == []:
                return False 
            elif c in pairs.values():
                stack.append(c)
            elif pairs[c] == stack.pop():
                continue
            else :
                return False 
        return stack is not None 






        