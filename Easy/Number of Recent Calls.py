# https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        
        self.counter = []

    def ping(self, t: int) -> int:
        
        self.counter.append(t)
        
        to_remove = []
        
        for i in self.counter:
            if t - i > 3000:
                to_remove.append(i)
        
        for j in to_remove:
            self.counter.remove(j)
        
        return len(self.counter)
    

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
