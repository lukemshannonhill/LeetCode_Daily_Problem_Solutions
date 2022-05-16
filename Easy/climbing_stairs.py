# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        
        ways = [1,2]
        
        if n < 3:
            return ways[n-1]
        
        while len(ways) < n:
            ways.append(ways[-1]+ways[-2])
        
        return ways[n-1]
