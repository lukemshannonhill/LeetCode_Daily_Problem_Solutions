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
        
        ```
        My first solution was a brute force method which encountered a Time Limit Exceeded exception. I've included it below:
        
        class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        i = intervals
        
        i.sort()
        
        # Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.
        
        # (a, b) and (c, d)
        
        # c <= a
                        
        # b <= d
        
        # now we must check whether the second element of the first tuple (d) is greater than or equal to the second element
        # of the second tuple (b). If it is, remove the second tuple.
        
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
        ```
