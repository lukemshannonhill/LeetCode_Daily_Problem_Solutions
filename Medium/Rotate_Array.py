# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # check the trivial cases first: is k == 0 or k == len(nums)? If so, return nums
        
        if k == 0 or k == len(nums):
            return nums
        
        # then check if len(nums) > k. If so, take k % len(nums)
        
        t = None
        
        if k > len(nums):
            t = k % len(nums)
            
        if t != None:
            k = t
            
        numz = nums[len(nums) - k:] + nums[:len(nums)-k]
        
        for i in range(len(numz)):
            nums[i] = numz[i]
        
        
