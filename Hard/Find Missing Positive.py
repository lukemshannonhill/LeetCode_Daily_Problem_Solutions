# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # checks the base case
        
        if nums == []:
            return 1
        
        s = set()
        
        for i in nums:
            s.add(i)
            
        next = 1
        
        for i in range(1, (len(nums)+1)):
            if i not in s:
                return i
            else:
                next += 1
        
        return next
