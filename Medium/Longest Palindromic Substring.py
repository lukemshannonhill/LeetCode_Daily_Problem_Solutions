# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n, answer = len(s), ''
        
        def helper(i,j):
            while i >= 0 and j < n and s[i] == s[j]:
                i, j = i -1, j + 1
            return s[i+1:j]
        
        for k in range(n):
            answer = max(helper(k,k), helper(k,k+1), answer, key=len)
        return answer
