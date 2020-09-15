class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        count = 0
        
        # Ensure no leading or trailing spaces so that the simple logic I've outlined below works as intended
        
        s = s.strip()
        
        for i in range(len(s)):
            if s[i] == ' ':
                count = 0
            else:
                count += 1
                
        return count
