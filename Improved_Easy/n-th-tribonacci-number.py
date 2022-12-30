# https://leetcode.com/problems/n-th-tribonacci-number/submissions/868237721/

class Solution:
    def tribonacci(self, n: int) -> int:
        
        abc = [0,1,1]
        
        if n < 3:
            return abc[n]
                
        while len(abc)-1 < n:
            l=len(abc)
            abc.append(abc[l-1]+abc[l-2]+abc[l-3])
            
        return abc.pop()
