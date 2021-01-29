# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        s = 'a'*n
        
        if k == n:
            return s
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        d = {key:value for key, value in enumerate(alphabet)}
        
        k = k-n
        
        z = []
        
        for i in s:
            z.append(i)
        
        i = len(s) - 1
        
        while k != 0:
            while k >= 25:
                z[i] = 'z'
                k -= 25
                i -= 1
            if k == 0:
                break
            else:
                z[i] = d[k]
                k = 0
        
      #  print(z)
        
        s = ''
        
        for i in z:
            s = s + i 
            
        return s
