# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        count = 0
        first_one = False
        
        for i in nums:
            if i == 1:
                if first_one == False:
                    first_one = True
                elif count < k:
                    return False
                elif count >= k:
                    count = 0
            else:
                if first_one == False:
                    continue
                else:
                    count += 1
                    
        return True
        
