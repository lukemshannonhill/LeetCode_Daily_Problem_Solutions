# https://leetcode.com/problems/search-insert-position
'''
Runtime
146 ms
Beats
5.3%
Memory
14.5 MB
Beats
97.73%
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target not in nums:
            i = target
            if target > nums[0]:
                while i not in nums:
                    i -= 1
                    if i in nums:
                        return nums.index(i) + 1
            else:
                while i not in nums:
                    i += 1
                    if i in nums:
                        if nums.index(i) == 0:
                            return 0
                        else:
                            return nums.index(i) - 1   

        return nums.index(target)
