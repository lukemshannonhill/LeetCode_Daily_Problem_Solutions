# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
                
        dummy = ListNode()
        dummy.next = head
        
        current = head
        previous = dummy
        
        while current and current.next:
            
            if current.val == current.next.val:
                
                while current.next and current.val == current.next.val:
                    
                    current = current.next
                    previous.next = current.next
                    
                current = current.next 
                
            else:
                
                previous = current
                current = current.next
                
        return dummy.next
