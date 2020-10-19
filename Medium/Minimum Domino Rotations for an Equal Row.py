# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        # if flips are possible, then we can flip everything
        
        top = [[0],[0],[0],[0],[0],[0]]
        
        bottom = [[0],[0],[0],[0],[0],[0]]
        
        duplicates = [[0],[0],[0],[0],[0],[0]]
        
        for i in range(len(A)):
        
            if A[i] != B[i]:  
                top[A[i]-1][0] += 1
                bottom[B[i]-1][0] += 1
                
            else:
                duplicates[A[i]-1][0] += 1
                                
        # now check the trivial case: if no flips are needed, return 0. no flips are needed if any single digit count in either the top or the bottom row has value equal to the length of A (or B)
        
        for j in top:
            if j == len(A):
                return 0
            
        for k in bottom:
            if k == len(B):
                return 0
            
        # if top[i] + bottom[i] == len(A) then it is a candidate solution. If no candidtae solutions exist, return -1:
        
        candidates = []
        
        for m in range(len(top)):
            if top[m][0] + bottom[m][0] + duplicates[m][0] == len(A):
                candidates.append(m)
        
        if candidates == []:
            return -1
        
        # now, of the candidate solutions, we see which absolute difference between top[candidate[m]] and bottom[candidate[m]] is the least
        
        differences = []
        
        for n in candidates:
            differences.append(abs(top[n][0] - bottom[n][0]))
            
        # now I have n candidate differences. I need to find the smallest value in candidates. That gives me the position in both top and bottom I'll need to check. I'll return the smallest value between those values.
        
        index = differences.index(min(differences))
        
        return min(top[candidates[index]][0], bottom[candidates[index]][0])
        
