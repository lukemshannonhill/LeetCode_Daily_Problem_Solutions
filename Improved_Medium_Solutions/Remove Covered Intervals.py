
# https://leetcode.com/problems/remove-covered-intervals/

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        i = intervals
        
        i.sort(key = lambda x: (x[0], -x[1]))
                
        right_so_far = i[0][1]
        
        count = 1
        
        for j in i:
            
            if j[1] > right_so_far:
                
                right_so_far = j[1]
                count += 1

        return count
