# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1:
            return 1
                
        a = [0,1]
        
        i = 1 
        
        while i < n:
            i = i + 1
            b = a[i-1] + a[i-2]
            a = a + [b]
            
        return a[i]
        
# reattempt, 5/14/22:
'''
class Solution:
    def fib(self, n: int) -> int:
        
        if n <= 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
'''
