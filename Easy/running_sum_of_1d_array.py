# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        total = 0
        returns = []
        
        for i in nums:
            total += i          
            returns.append(total)

        return returns
