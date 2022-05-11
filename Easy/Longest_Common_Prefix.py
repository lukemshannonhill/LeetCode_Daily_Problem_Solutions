# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        max_length = 201 
        
        for i in range(len(strs)):
            if len(strs[i]) < max_length:
                max_length = len(strs[i])
                position = i
        
        returns = strs[position]
        
        for i in range(len(strs)):
            
            l = len(strs[i])
            
            for j in range(0, l):
                
                if j > len(returns)-1:
                    break
                elif returns[j] == strs[i][j]:
                    continue
                else:
                    returns = returns[:j]
        
        return returns 
            
