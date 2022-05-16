# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        minimum_cost = [0] * (len(cost)+1)
        
        for i in range(2, len(cost)+1):
            one = minimum_cost[i-1] + cost[i-1]
            two = minimum_cost[i-2] + cost[i-2]
            minimum_cost[i] = min(one, two)
            
        return minimum_cost[-1]
