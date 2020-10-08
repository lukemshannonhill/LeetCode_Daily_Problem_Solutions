# https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # this is a brute force solution
        
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        return -1
