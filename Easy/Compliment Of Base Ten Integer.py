# https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        
        binary_array = bin(N)
        
        binary_array = binary_array[2:]
        
        compliment = []
        
        for i in binary_array:
            if i == '1':
                compliment.append(0)
            else:
                compliment.append(1)
        
        powers = len(compliment) - 1
        final = 0
        
        for j in compliment:
            if j == 1:
                final += 2**powers
                powers -= 1
            else:
                powers -= 1
                
        return final
                
