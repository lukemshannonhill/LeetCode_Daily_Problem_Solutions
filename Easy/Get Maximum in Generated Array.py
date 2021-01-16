# https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        # nums[0] = 0
        # nums[1] = 1
        # nums[2 * i] = nums[i] when 2 <= 2 * i <= n
        # nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n

        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        nums = [0]*(n+2)
        nums[1] = 1
        
        for i in range(2, n+1):
            if i % 2 == 0:
                nums[i] = nums[i//2]
            else:
                nums[i] = nums[i//2] + nums[i//2 + 1]
                
        return max(nums[:n+1])
