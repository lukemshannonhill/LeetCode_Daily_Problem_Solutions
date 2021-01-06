# https://leetcode.com/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        c = []
        l = len(arr)

        for i in range(1, 2001):
            c.append(i)
            
        pointer_to_c = 0
        pointer_to_arr = 0
        
        counter_to_k = 0
        
        # I have my reference array, c.
        
        # I must now compare, element wise, c and arr.
        
        # Either they match or they don't. If they match, then I increment the pointer to c and the pointer to arr by one and continue.
        
        # If they don't match, then I increment my counter_to_k by one and increment my pointer_to_c by one.
                
        while counter_to_k < k:
            
            if pointer_to_arr == l:
                counter_to_k += 1
                last_seen_missing = c[pointer_to_c]
                pointer_to_c += 1
                
            elif c[pointer_to_c] == arr[pointer_to_arr]:
                    pointer_to_c += 1
                    pointer_to_arr += 1
            else: 
                counter_to_k += 1
                last_seen_missing = c[pointer_to_c]
                pointer_to_c += 1
        
        return last_seen_missing
