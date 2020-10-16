# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # So my initial idea is to walk down the first element of each row until I find a number that is greater than our target
        
        # If I do, then the target must be in the previous row and so I can simply scan that previous row for the target.
        
        # If the target does not appear in that row, then the target does not appear in the matrix. 
        
        # If I don't find a first value that's larger than the target, then I walk down the last row to see if the target
        
        # is simply contianed in the last row. If I don't find the target in this way, then the target is not contained
        
        # in the matrix. 
        
        # We can optimize the search of the rows, but let's simply code up the above solution first and see how it compares
        
        # to other submissions.
        
        # i's are rows, j's are columns
        
        # First, we must check whether the matrix is empty (it's a base case and breaks our below logic if passed to it)
        
        if matrix == [[]]:
            
            return False
        
        # Now, check the case where the m x n matrix is an m x 1 matrix:
        
        if len(matrix) == 1:
            for i in matrix[0]:
                if i == target:
                    return True
            return False
        
        for i in range(len(matrix)):
            if matrix[i][0] == target:
                
                # a trivial case: is the first element we're checking the target? If so, return True
                
                return True
            
            elif matrix[i][0] > target and i == 0:
                
                # another base case: If the first eleemnt of the first row is greater than the target, then by construction
                # the target can't be contianed in the matrix. Return False.
                
                return False
            
            elif matrix[i][0] < target and i != len(matrix)-1:
                
                # If the first element of the row is less than the target, then we'll continue walking down the rows (as long
                # as we're not considering the last row).
                
                continue 
                
            elif matrix[i][0] > target:
            
            # This is the case I expect to fire most often: we walk down the previous row's values if the first element of the 
            # current row is larger than target (and none of the above conditionals have triggered, of course).
            
                for j in range(len(matrix[i-1])):
                    if matrix[i-1][j] == target:
                        return True
                
                # If we exhuast this loop, we return False (this follows by construction/the properties of the matrix)
                
                return False
            
            elif matrix[i][0] < target and i == len(matrix)-1:
                for j in matrix[i]:
                    if j == target:
                        return True
                return False
            
            
