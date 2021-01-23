# https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        # First check to ensure the strings are of the same length. If they're not, return False.
        
        if len(word1) != len(word2):
            return False
        
        # Next, ensure that the alphabet of characters used in each string are the same. If they're not, return False.
        
        d1 = {key:value for value, key in enumerate(word1)}
        
        d2 = {key:value for value, key in enumerate(word2)}
        
        if d1.keys() != d2.keys():
            return False
        
        # Operation one simply means that the particular order of characters doesn't matter. Only their total number of occurances in the string does.
        
        # So the idea is: if the strings share the same alphabet, then count the number of occurences of each unique character in each string (e.g., if word1 = "aabccc" and word2 = "abbbcc" then the strings share the same alphabet and each word has 1 occurance of one unique character, 2 occurances of another unique character, and three occurances of a third unique character). If this "occurence count" is the same, then the strings can be made into one another and we return True.
        
        o1 = {}
        
        for i in word1:
            if i not in o1:
                o1[i] = 1
            else:
                o1[i] += 1
                
        o2 = {}
        
        for i in word2:
            if i not in o2:
                o2[i] = 1
            else:
                o2[i] += 1
        
        l1 = []
        
        for i in o1.values():
            l1.append(i)
        
        for i in o2.values():
            if i not in l1:
                return False
            else:
                l1.remove(i)
        
        return True
