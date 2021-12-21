# https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        
        a = [0,1,1,2]
        
        if n < 4:
            return a[n]
        
        i = 3
        
        while i < n:
            i = i + 1
            b = a[i-1]+a[i-2]+a[i-3]
            a = a+[b]
            
        return a[n]
