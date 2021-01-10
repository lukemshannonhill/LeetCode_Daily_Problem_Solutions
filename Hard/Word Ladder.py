# https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        
        l = len(beginWord)
        
        d = defaultdict(list)
        
        for word in wordList:
            for i in range(l):
                d[word[:i] + "*" + word[i+1:]].append(word)
        
        q = collections.deque([(beginWord, 1)])
        
        visited = {beginWord: True}
        
        while q:
            current_word, depth = q.popleft()
            for i in range(l):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                
                for word in d[intermediate_word]:
                    if word==endWord:
                        return depth + 1
                    if word not in visited:
                        visited[word] = True
                        q.append((word, depth +1))
                d[intermediate_word] = []
                
        return 0
        
        
        
        
