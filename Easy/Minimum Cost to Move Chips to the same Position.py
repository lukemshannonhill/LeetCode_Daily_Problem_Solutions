# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        
        d = {}
        
        for i in position:
            if i not in d:
                d[i] =  1
            else:
                d[i] += 1
        
        odds = 0 
        evens = 0
        
        for key in d:
            if key % 2 == 0:
                evens += d[key]
            else:
                odds += d[key]
                
        if odds == evens:
            return odds
        
        if odds > evens:
            return evens
        else:
            return odds
            
