# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        occurance, returns = collections.defaultdict(int), 0
        
        for n in nums:
            
            if occurance[k-n]:
                
                occurance[k-n] -= 1
                returns += 1
                
            else:
                
                occurance[n] += 1
                
        return returns 
