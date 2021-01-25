# https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        # Create a new linked list to be returned--we will return returns.next
              
        l = len(lists)
        
        if l == 0:
            return None
        if l == 1:
            return lists[0]
        
        for i in range(len(lists)):
            if lists[i] != lists[0]:
                break
            if i == len(lists) - 1:
                return lists[0]
        
        returns = head = tail = ListNode()
        
        head.next = ListNode()
        
        head = head.next
        
        while True:
            
            # set min to infinity
            min = float(inf)
            
            for i in lists:
                
                #traverse the list to find the smallest value
                if i != None:
                    if i.val < min:
                        min = i.val
                
            
            # advance the linked list containing i to the next node
            operated = False
            
            for j in range(len(lists)):
                if lists[j] != None:
                    if lists[j].val == min and operated == False:
                        lists[j] = lists[j].next
                        operated = True
                        break
            

            if min == float(inf):
                while tail.next.val != None:
                    tail = tail.next
                tail.next = None
                return returns.next
            
            head.val = min
            head.next = ListNode(val=None)
            head = head.next
