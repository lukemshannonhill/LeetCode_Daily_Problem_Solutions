# https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        from sortedcontainers import SortedList
        mod = 10**9 + 7
        
        returns = 0
        
        sorted_array = SortedList()
        for n in instructions:
            cost = min(sorted_array.bisect_left(n), len(sorted_array) - sorted_array.bisect_right(n))
            returns = (returns + cost) % mod
            sorted_array.add(n)
            
        return returns 
