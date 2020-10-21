# LeetCode_Daily_Problem_Solutions

This is a respository containing my Python3 solutions to [LeetCode's](https://www.leetcode.com) daily problems. 

I intend to revist each problem at least once to improve upon my intial solution, although I want at least a day to pass between writing my initial solution and attempting an improved solution. The notes column will call out either items I'd like to attend to on an attempt at an improved solution or else will contain snippets of things I learned or found useful in solving the problem more elegantly.

| Problem | Initial Solution | Improved Solution | Notes | 
| --- | --- | --- | --- |
|      https://leetcode.com/problems/length-of-last-word/   |    [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Length%20of%20Last%20Word.py)         | --- | To do: Construct a more elegant, one line solution exploiting existing string methods more fully |
| https://leetcode.com/problems/word-break/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Word%20%20Break.py) | --- | I'm certain the optimal solution uses tries. After reviewing tries I'll reattempt this problem. https://en.wikipedia.org/wiki/Trie |
| https://leetcode.com/problems/first-missing-positive/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Hard/Find%20Missing%20Positive.py) | --- | Although my initial solution is accepted by leetcode, I'm utilizing memory the optimal solution almost certainly wouldn't. Upon revisiting this problem, I'd like to ensure I utilize as little memory as possible (perhaps performing in place operations on the array?). |
| https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3480/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Number%20of%20Recent%20Calls.py) | --- | The "to_remove" list is cumbersome and inelegant. I would like to use a queue when reattempting this problem. |https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3480/https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3480/ |
| https://leetcode.com/problems/combination-sum/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Combination%20Sum.py) | --- | I'd like to solve this in another way upon my reattempt. |
| https://leetcode.com/problems/k-diff-pairs-in-an-array/description/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/K-diff%20Pairs%20in%20an%20Array.py) | --- | To do: Improve time complexity |
| https://leetcode.com/problems/remove-covered-intervals/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Initial%20Solutions/Medium/Remove%20Covered%20Intervals.py) | [Improved Soltuion](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Remove%20Covered%20Intervals.py) | I'd like to write a solution that modifies the "intervals" list in place by deleting out intervals that are encompassed by some other interval in the list |
| https://leetcode.com/problems/complement-of-base-10-integer/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Compliment%20Of%20Base%20Ten%20Integer.py) | --- | Upon my reattempt I would like to avoid using the bin() funciton. It was convienent but I think building the machinery myself to convert from base ten to binary would be more helpful practice than simply invoking a function I already know about. |
| https://leetcode.com/problems/insert-into-a-binary-search-tree/ | [Initial Soltuion](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Insert%20into%20a%20Binary%20Search%20Tree.py) | --- | Note: This solution initially unexpectedly failed. I suspect a bug in the leetcode platform? An empty tree was passed as a test case and insert function I wrote didn't handle it appropriately (namely, the if clause that checks whether the root node is None didn't seem to fire). An acceptance was achieved after simply including that if clause again at the end of the program. I'd like to test this further and understand why this unexpected behavior is occuring. |
| https://leetcode.com/problems/binary-search/description/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Binary%20Search.py)| --- | My initial solution is a brute force method. I would like to implement binary search upon my reattempt. |
| https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Minimum%20Domino%20Rotations%20for%20an%20Equal%20Row.py) | --- | This solution beat almost 80% of Python3 solutions. I'd like to improve this measure. |
| https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3496/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Rotate_Array.py) | --- | My initial solution doubles the total memory usage required by constructing the solution array out of the appropriate slices of the original array and then copying, element wise, this solution array over the original array. It's an inelegant solution that permited me to quickly solve the problem using the slice syntax I'm familiar with. Upon my reattempt I should like to do away with this second array and simply operate on the original array in-place. |
| https://leetcode.com/problems/search-a-2d-matrix/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Search_a_2d_matrix.py) | --- | There are some optimizations that can be made in searching the rows for values (treat each row as a binary search, which it is by construciton). |
| https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Minimum%20Domino%20Rotations%20for%20an%20Equal%20Row.py) | --- | This solution beat almost 80% of Python3 solutions w/r/t time complexity. I'd like to improve that measure upon my reattempt. | 
| https://leetcode.com/problems/clone-graph/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Clone%20Graph.py) | --- | I'd like to implement a DFS method next. |
