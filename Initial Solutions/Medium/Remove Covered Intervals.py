# https://leetcode.com/problems/remove-covered-intervals/

# This is my initial solution, which encountered a Time Limit Exceeded error (understandably enough, since it's 
# a brute force solution). 

# I improved upon this solution day of in order to meet the requirements of the October LeetCoding Challenge.

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        i = intervals
        
        i.sort()
        
        # Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.
        
        # (a, b) and (c, d)
        
        # c <= a
                        
        # b <= d
                
        to_delete = []
        
        for j in i:
            for k in i:
                if k == j:
                    continue
                elif k[0] <= j[0] and j[1] <= k[1]:
                    if j not in to_delete:
                        to_delete = to_delete + [j]
        
        final = []
        
        for u in intervals:
            if u not in to_delete:
                final.append(u)
            
        return len(final)
            
                    
                    

