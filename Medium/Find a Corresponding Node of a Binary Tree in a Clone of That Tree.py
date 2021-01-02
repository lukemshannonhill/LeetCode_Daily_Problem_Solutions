# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        if target == cloned:
            return cloned 
        
        frontier = []
        
        while target.val != cloned.val:
            if cloned.left != None:
                frontier.append(cloned.left)
            if cloned.right != None:
                frontier.append(cloned.right)
            if frontier != []:
                cloned = frontier.pop()
            
        return cloned
