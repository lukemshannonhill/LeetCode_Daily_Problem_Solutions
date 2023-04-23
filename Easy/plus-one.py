''' 

https://leetcode.com/problems/plus-one/

Runtime
37 ms
Beats
40.99%
Memory
14 MB
Beats
5.53%

'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = 1
        add_a_place = False

        for i in range(len(digits)):
            if digits[i] != 9:
                digits[i] += carry
                carry = 0
            else:
                digits[i] += carry
                if digits[i] == 10:
                    digits [i] = 0
                    carry = 1
                    if len(digits) - 1 == i:
                        add_a_place = True

        s = set()
        for j in digits:
            s.add(j)
        
        z = set()
        z.add(0)

        if s.symmetric_difference(z) == set():
            digits.append(1)
            digits.reverse()
            return digits
        elif add_a_place == True:
            digits.append(1)
            digits.reverse()
            return digits 
        else:
            digits.reverse()
            return digits
