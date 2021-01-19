# https://leetcode.com/problems/max-number-of-k-sum-pairs/

# TLE

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        while nums[-1] >= k:
            nums.pop()
            
        count = 0
        
        n = nums
        
        nums =[]
        
        for j in n:
            nums.append([j, False])
            
        iterator = 0
        
        while nums:
            for i in nums:
                l = len(nums)
                # print(i)
                # print(nums)
                if nums == []:
                    return count
                if i[0] + nums[-1][0] == k and len(nums) > 1 and i[1] == False and nums[-1][1] == False and iterator != l:
                    i[1] = True
                    nums[-1][1] = True
                    count += 1
                    iterator += 1
                else:
                    iterator += 1
                    if iterator == l:
                        nums.pop()
                        iterator = 0
                        
        return count
