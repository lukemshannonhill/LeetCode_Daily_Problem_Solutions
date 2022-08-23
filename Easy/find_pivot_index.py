# https://leetcode.com/problems/find-pivot-index/submissions/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
                   
        right_total = 0
        left_total = 0
        
        for i in nums:
            right_total += i
            
        if right_total - nums[0] == 0:
            return 0
            
        for i in range(len(nums)):
            left_total += nums[i]
            right_total -= nums[i]
            
            if i == len(nums)-1:
                return -1
  
            if left_total == right_total - nums[i+1]:
                return i+1
            
