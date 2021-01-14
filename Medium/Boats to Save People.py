# Boats to Save People

# https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
                        
        p = people
        
        boat_count = 0
        
        g = 0
        
        while p:
            if limit - p[-1] != 0:
                if len(p) == 1:
                    return boat_count + 1 
                g = limit - p[-1]
                two_people_taken = False
                while g != 0:
                    if g in p[:-1]:
                        boat_count += 1
                        p.remove(g)
                        p.pop()
                        g = 0
                        two_people_taken = True
                        break
                    else:
                        g -= 1
                if two_people_taken == True:
                    two_people_taken = False
                else:
                    boat_count += 1
                    p.pop()
                    
            else:
                boat_count += 1
                p.pop()
                
        return boat_count
        
        # This returns a TLE error. 73 of 77 test cases completed. I'll need to speed it up. I'm going to try with a binary search.
