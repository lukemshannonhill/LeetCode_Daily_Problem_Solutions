# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps (self, num: int) -> int:
        
        if num == 0:
            return 0
        
        count = 0
        
        while num != 0:
            if num % 2 == 0:
                count += 1
                num = num//2
                
            else:
                count += 1
                num = num - 1
                
        return count
