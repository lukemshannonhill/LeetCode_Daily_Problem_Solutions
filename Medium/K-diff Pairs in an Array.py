# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        pairs = []
        
        for i in range(len(nums)):
            j = nums[i] + k
            for l in range(i, len(nums)):
                if nums[l] == j and i != l:
                    pairs.append([nums[i],nums[l]])
        
        # so now we have a list with possible duplicates. We need to remove the duplicates if they exist
        
        final = []
        
        for i in pairs:
            if i not in final:
                final.append(i)

        return len(final)
