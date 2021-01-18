# https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        dp = [1]*5
        
        for k in range(n):
            
            for v in range(1,5):
                
                dp[v] += dp[v-1]
                
        return dp[-1]
