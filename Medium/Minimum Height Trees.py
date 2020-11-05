# https://leetcode.com/problems/minimum-height-trees/

from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        remaining_nodes = n
        
        # check a base case
        
        if remaining_nodes == 1:
            return[0]
        
        # check another base case:
        
        if remaining_nodes == 2:
            return edges[0]
        
        adjacency_matrix = defaultdict(set)
        
        for source_node, destination_node in edges:
            adjacency_matrix[source_node].add(destination_node)
            adjacency_matrix[destination_node].add(source_node)
            
        leaf_nodes = [node for node in adjacency_matrix if len(adjacency_matrix[node]) == 1]
        
        while remaining_nodes > 2:
            
            remaining_nodes -= len(leaf_nodes)
            
            next_bunch_of_leaves = []
            
            for leaf in leaf_nodes:
                
                neighbor = adjacency_matrix[leaf].pop()
                adjacency_matrix[neighbor].remove(leaf)
                
                if len(adjacency_matrix[neighbor]) == 1:
                    next_bunch_of_leaves.append(neighbor)
                    
                leaf_nodes = next_bunch_of_leaves
                
        return leaf_nodes
