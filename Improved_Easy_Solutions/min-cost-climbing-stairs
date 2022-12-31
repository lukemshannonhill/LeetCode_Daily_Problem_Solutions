# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)+1
        m = [0]*(l)

        for i in range(2, l):
            take_one_step = m[i - 1] + cost[i - 1]
            take_two_steps = m[i - 2] + cost[i - 2]
            m[i] = min(take_one_step, take_two_steps)
        
        return m[-1]
