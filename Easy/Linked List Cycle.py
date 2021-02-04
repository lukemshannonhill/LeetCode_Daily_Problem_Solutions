# https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if head is None or head.next is None:
            return False
        
        count = 0 
        
        m = 10**4 + 2
        
        while head.next != None and count < m:
            count += 1
            head = head.next
            
        if count >= m:
            return True
        else:
            return False
        

