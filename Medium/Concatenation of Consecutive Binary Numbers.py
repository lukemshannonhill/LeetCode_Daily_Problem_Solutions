# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        s = ''
        
        for i in range(1, n+1):
            b = bin(i)
            s = s + b[2:]
            
        def btd(n):
            return int(n,2)
        
        m = 10**9 + 7
        
        return btd(s) % m
