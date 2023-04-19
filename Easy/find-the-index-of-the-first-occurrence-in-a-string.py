# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
'''
Runtime
27 ms
Beats
88.93%
Memory
13.8 MB
Beats
50.18%

'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle not in haystack:
            return -1
        else:
            return haystack.find(needle)
        '''
        m = 0

        if needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)):
                if haystack[i] == needle[0]:
                    for j in range(len(needle)):
                        if haystack[i+j] == needle[j]:
                            m = j
                    if m + i == i + len(needle):
                        return i
'''
                    
