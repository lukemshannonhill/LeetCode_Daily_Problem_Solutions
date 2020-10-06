# https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        # I'll walk through my thinking w/r/t this problem prior to coding.
        
        # First I need to traverse the BST to find the appropriate insertion location 
        
        # to do so I will start with the root node and begin by checking whether there's a val
        
        # if no val, it's trivial: Just insert the new val and return the root node.
        
        # If val < TreeNode.val, then we'd go left (recursively)
        
        # If val > TreeNode.val, then we'd go right (recursively)
        
        # Eventually we arrive at a node with either one, two, or no children 
        
        # So, let's enumerate all of the cases:
        
        # Consider, concretely, the following example: Parent.val = 10. Parent.left.val = 5. Parent.right.val = 15.
        
        # The value given could be less than five. If so, we'd overwrite one of the None child nodes of 5 with a new tree node
        # containing the value given.
        
        # The value given could be greater than five but less than ten. Same story as above w/r/t overwriting the child None
        # node (but this time, obviously, overwrite the Right child None node).
        
        # The value given could be greater than 10 but less than 15: Overwrite the Left None child node of 15.
        
        # The value given could be greater than 15: Overwrite the Right None child node of 15.
        
        # Arriving at a leaf node with no non-None children is the simpliest case: Just overwrite one of the None child nodes
        # as described above
        
        # Suppose we arrive at a node with one None child and one non-None child. That treatment is just a mix of the above two
        # cases, depending upon what the given val is and where the None child resides. In any case, we'll be overwriting a 
        # None child.
        
        def insert(root, node):
            if root is None:
                root = node
            else:
                if root.val < node.val:
                    if root.right is None:
                        root.right = node
                    else:
                        insert(root.right, node)
                else:
                    if root.left is None:
                        root.left = node
                    else:
                        insert(root.left, node)
        
        node = TreeNode(val)
              
        insert(root, node)
        
        if root is None:
            root = TreeNode(val)
        
        return root
        
