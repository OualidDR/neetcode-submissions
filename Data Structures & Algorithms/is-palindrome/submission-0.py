class Solution:
    def isPalindrome(self, s: str) -> bool:
        #i have to ignore all non-alphanumeric characters 
        l =[ch.lower() for ch in s if ch.isalnum()]
        return l == l[::-1]