# https://leetcode.com/problems/find-the-most-competitive-subsequence/

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        tries = len(nums) - k
        stack = []
        for n in nums:
            while stack and n < stack[-1] and tries > 0:
                stack.pop()
                tries -= 1
            stack.append(n)
        
        return stack[:k]
