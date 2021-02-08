# https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        previous = float('-inf')
        ans = []
        for i, x in enumerate(s):
            if x == c:
                previous = i
            ans.append(i - previous)
                
        previous = float('inf')
        for i in range(len(s) -1, -1, -1):
            if s[i] == c: 
                previous = i
            ans[i] = min(ans[i], previous - i)
                
        return ans
