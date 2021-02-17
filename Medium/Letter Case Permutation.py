# https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        return map(''.join, product(*[set([i.lower(), i.upper()]) for i in S]))
        
