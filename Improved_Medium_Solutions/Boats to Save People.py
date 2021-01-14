# https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
                                    
        people.sort()

        start, finish, total_boats = 0, len(people) - 1, 0
        
        while start <= finish:
            
            if people[start] + people[finish] <= limit:
                start += 1
            
            total_boats += 1
            
            finish -= 1
            
        return total_boats
