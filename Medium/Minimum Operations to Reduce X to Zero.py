# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        
        # we must pass through at least either the first or the last element in n in order to solve this problem. If both are too large to "pass through," well... the game's up!
        
        if nums[-1] > x and nums[0] > x:
            return -1
        
        num_sum = sum(nums)
        
        if num_sum < x:
            return -1
        
        if num_sum == x:
            return len(nums)
        
        max_subarray_total = num_sum - x
        left = current_sum = size_so_far = 0
        for right, n in enumerate(nums):
            
            current_sum += n
            
            while current_sum > max_subarray_total:
                current_sum -= nums[left]
                left += 1
            
            if current_sum == max_subarray_total:
                size_so_far = max(size_so_far, right - left + 1)
                print(max_subarray_total)
        return len(nums) - size_so_far if size_so_far != 0 else -1
