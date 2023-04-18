# https://leetcode.com/problems/remove-element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #n = [x for x in nums if x != val]
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums.remove(val)
                i -= 1
        return len(nums)
