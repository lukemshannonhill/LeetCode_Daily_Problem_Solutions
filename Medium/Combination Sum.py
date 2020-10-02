# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        c = candidates 
        
        c.sort()
        
        t = target
        
        r = []
        
        left_overs = 0
        
        def dfs(left_overs, stack):
            if left_overs == 0:
                r.append(stack)
                return
            
            for i in c:
                if i > left_overs:
                    break
                if stack and i < stack[-1]: 
                    continue
                else:
                    dfs(left_overs - i, stack + [i])
            
        dfs(t, [])
        
        return r  
