# https://leetcode.com/problems/check-array-formation-through-concatenation/

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:

        result = []
        
        for j in arr:
            for i in pieces:
                if i[0] == j:
                    for m in range(len(i)):
                        result.append(i[m])
                        
        if result == arr:
            return True
        else:
            return False
