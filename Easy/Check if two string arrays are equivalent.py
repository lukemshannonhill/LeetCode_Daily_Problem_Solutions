# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        a = ''
        b = ''
        
        for i in word1:
            a = a + i
            
        for j in word2:
            b = b + j
        
        if a == b:
            return True
        else:
            return False
