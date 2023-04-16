# https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while True:
            if len(nums) == i:
                return len(nums)
            while nums[i] == nums[i-1]:
                nums.pop(i)
                if len(nums) == i:
                    return len(nums)

            i+=1
