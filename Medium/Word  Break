# https://leetcode.com/problems/word-break/

# This solution fails to pass all tests. I'm certain that the right implementaiton uses tries.

# https://en.wikipedia.org/wiki/Trie

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        bank = set()
        
        for i in range(len(wordDict)):
            bank.add(wordDict[i])
            
        temp = ''
        used = set()
        tries = 0
        result = False
        
        while tries < (len(s)):
            for i in range(len(s)):
                temp += s[i]
                
                if temp in bank:
                    if temp not in used:
                        used.add(temp)
                    temp = ''
            
                    if i == (len(s)-1) and (temp == '' or temp in used):
                        return True
                if i == (len(s)-1):
                    tries = tries + 1
                    temp = ''
                    
        return False
