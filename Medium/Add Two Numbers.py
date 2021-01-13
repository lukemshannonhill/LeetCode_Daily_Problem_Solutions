 # https://leetcode.com/problems/add-two-numbers/
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0
        
        dummyHead = head = ListNode()
        
        while l1!= None or l2!= None or carry > 0:
            
            if l1 != None:
                carry += l1.val
                l1 = l1.next
                
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            
            head.next = ListNode(carry % 10)
            head = head.next
            carry //= 10
        
        return dummyHead.next
