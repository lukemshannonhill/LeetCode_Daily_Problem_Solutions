# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        string_so_far = []
        
        max_length = 0
        
        returns = []
        
        for i in s:
            if i in string_so_far:
                while i in string_so_far:
                    string_so_far = string_so_far[1:]
                string_so_far.append(i)
                l = len(string_so_far)
                max_length = max(max_length, l)
                if l == max_length:
                    returns = string_so_far
                    
            else:
                string_so_far.append(i)
                l = len(string_so_far)
                max_length = max(max_length, l)
                if l == max_length:
                    returns = string_so_far
        
        return len(returns)
        
