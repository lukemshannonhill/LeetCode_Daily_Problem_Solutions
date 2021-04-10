# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        d = {k:v for v, k in enumerate(order)}
        d['_'] = -1
        
        for w, wprime in zip(words, words[1:]):
            for c, cprime in zip_longest(w, wprime, fillvalue='_'):
                check = d[c] - d[cprime]
                if check > 0: return False
                if check < 0: break
        
        return True
        
