# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        while k > 1:
            nums.pop()
            k -= 1
        
        return nums.pop()
