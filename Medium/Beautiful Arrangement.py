# https://leetcode.com/problems/beautiful-arrangement/

class Solution:
    def countArrangement(self, n: int) -> int:
       
        def solver(current):
            if len(current) == 1:
                return 1
        
            total = 0
            
            for j in range(len(current)):
                if current[j] % len(current) == 0 or len(current) % current[j] == 0:
                    total += solver(current[:j] + current[j+1:])
            
            return total
        
        return solver(tuple(range(1, n+1)))

