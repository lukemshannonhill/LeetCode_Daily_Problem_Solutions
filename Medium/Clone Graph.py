# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        # check the base cases
        
        if not node:
            return node
        
        d = {node: Node(node.val)}
        
        frontier = collections.deque([node])
        
        while frontier:
            
            new = frontier.popleft()
            
            for neighbor in new.neighbors:
                if neighbor not in d:
                    frontier.append(neighbor)
                    d[neighbor] = Node(neighbor.val)
                d[new].neighbors.append(d[neighbor])
                
        return d[node]
