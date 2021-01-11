# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        length = len(nums1)
        
        if n == 0:
            return nums1
        
        index1 = []
        
        # remove trailing zeros
        
        while nums1[-1] == 0:
            nums1.pop()
            if nums1 == []:
                break
        
        for j in nums2:
            for i in range(len(nums1)):
                if j <= nums1[i]:
                    index1.append(i)
            if index1 == []:
                nums1.append(j)
            else:
                nums1.insert(index1[0], j)
                index1 = []
         
        # pad num1 back to size m if len(num1) < length (captured above as the length of the input nums1):
        
        while len(nums1) != length:
            nums1.append(0)
        
        return nums1
        
