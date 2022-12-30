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
| https://leetcode.com/problems/remove-covered-intervals/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Remove%20Covered%20Intervals.py) | [Improved Soltuion](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Improved_Medium_Solutions/Remove%20Covered%20Intervals.py) | I'd like to write a solution that modifies the "intervals" list in place by deleting out intervals that are encompassed by some other interval in the list |
| https://leetcode.com/problems/complement-of-base-10-integer/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Compliment%20Of%20Base%20Ten%20Integer.py) | --- | Upon my reattempt I would like to avoid using the bin() funciton. It was convienent but I think building the machinery myself to convert from base ten to binary would be more helpful practice than simply invoking a function I already know about. |
| https://leetcode.com/problems/insert-into-a-binary-search-tree/ | [Initial Soltuion](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Insert%20into%20a%20Binary%20Search%20Tree.py) | --- | Note: This solution initially unexpectedly failed. I suspect a bug in the leetcode platform? An empty tree was passed as a test case and insert function I wrote didn't handle it appropriately (namely, the if clause that checks whether the root node is None didn't seem to fire). An acceptance was achieved after simply including that if clause again at the end of the program. I'd like to test this further and understand why this unexpected behavior is occuring. |
| https://leetcode.com/problems/binary-search/description/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Binary%20Search.py)| --- | My initial solution is a brute force method. I would like to implement binary search upon my reattempt. |
| https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Minimum%20Domino%20Rotations%20for%20an%20Equal%20Row.py) | --- | This solution beat almost 80% of Python3 solutions. I'd like to improve this measure. |
| https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3496/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Rotate_Array.py) | --- | My initial solution doubles the total memory usage required by constructing the solution array out of the appropriate slices of the original array and then copying, element wise, this solution array over the original array. It's an inelegant solution that permited me to quickly solve the problem using the slice syntax I'm familiar with. Upon my reattempt I should like to do away with this second array and simply operate on the original array in-place. |
| https://leetcode.com/problems/search-a-2d-matrix/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Search_a_2d_matrix.py) | --- | There are some optimizations that can be made in searching the rows for values (treat each row as a binary search, which it is by construciton). |
| https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Minimum%20Domino%20Rotations%20for%20an%20Equal%20Row.py) | --- | This solution beat almost 80% of Python3 solutions w/r/t time complexity. I'd like to improve that measure upon my reattempt. | 
| https://leetcode.com/problems/clone-graph/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Clone%20Graph.py) | --- | I'd like to implement a DFS method next. |
| https://leetcode.com/problems/minimum-height-trees/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Minimum%20Height%20Trees.py) | --- | How would I solve this if I didn't know that there exist, at most, 2 Minimum Height Trees for any given graph? |
| https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Minimum%20Cost%20to%20Move%20Chips%20to%20the%20same%20Position.py) | --- | I'd like to decrease runtime |
|https://leetcode.com/problems/check-array-formation-through-concatenation/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/check%20array%20formation%20through%20concatenation.py) | --- | What's one improvement that could be made to decrease total runtime? 
| https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Find%20a%20Corresponding%20Node%20of%20a%20Binary%20Tree%20in%20a%20Clone%20of%20That%20Tree.py) | --- | This solution exploits the fact that these binary trees only contain distinct values. It would be better to write a program that could handle duplicate values. |
| https://leetcode.com/problems/beautiful-arrangement/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Beautiful%20Arrangement.py) | --- | Solve differently and explain tradeoffs. |
| https://leetcode.com/problems/merge-two-sorted-lists/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Merge%20Two%20Sorted%20Lists.py) | --- | I'd like to implement a solution that uses less memory. |
| https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Remove%20Duplicates%20From%20Sorted%20List%20II.py) | --- | What's another way of solving this? |
| https://leetcode.com/problems/kth-missing-positive-number/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Kth%20Missing%20Positive%20Number.py) | --- | The runtime of this solution beats only about 30% of entries. Write another solution that improves upon this. |
| https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3595/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Longest%20Substring%20Without%20Repeating%20Characters.py) | --- | This solution does well on total memeory usage but beats only about 20% of other solutions w/r/t time complexity. Write another solution that improves upon this. |
| https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Check%20if%20two%20string%20arrays%20are%20equivalent.py) | --- | My solution certainly isn't optimal. How might I solve this another way that makes at least one improvement in either space or time complexity? | 
| https://leetcode.com/problems/word-ladder/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Hard/Word%20Ladder.py) | --- | Try using tries. |
| https://leetcode.com/problems/create-sorted-array-through-instructions/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Hard/Create%20Sorted%20Array%20Through%20Instructions.py) | --- | I rely heavily here upon SortedList() and the bisect module. Would be good to independetly implement these both in the first rework of this problem. | 
| https://leetcode.com/problems/merge-sorted-array/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Merge%20Sorted%20Arrays.py) | --- | This solution is very much a first attempt and that fact is reflected in its considerable running time. Aim to push this metric down in a future rework. |
| https://leetcode.com/problems/add-two-numbers/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Add%20Two%20Numbers.py) | --- | How could I improve the runtime? The memory usage? |
| https://leetcode.com/problems/boats-to-save-people/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Boats%20to%20Save%20People.py) | [Improved Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Improved_Medium_Solutions/Boats%20to%20Save%20People.py) | What's another way I could write a solution that passes all test cases? Would binary search work in this case just as well as my improved solution? |
| https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Minimum%20Operations%20to%20Reduce%20X%20to%20Zero.py) | --- | How could I solve this in another way? |
| https://leetcode.com/problems/get-maximum-in-generated-array/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Get%20Maximum%20in%20Generated%20Array.py) | --- | How could I solve this by iteratively building the array with append? |
| https://leetcode.com/problems/kth-largest-element-in-an-array/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Kth%20Largest%20Element%20in%20an%20Array.py) | --- | This solution is fast (beating about 96% of other entries) but fails to beat more than about 45% of other entires re: memory usage. How could memory usage be improved? |
| https://leetcode.com/problems/count-sorted-vowel-strings/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Count%20Sorted%20Vowel%20Strings.py) | --- | How could I solve this differently? |
| https://leetcode.com/problems/max-number-of-k-sum-pairs/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Max%20Number%20of%20K%20Sum%20Pairs.py) | [Improved Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Improved_Medium_Solutions/Max%20Number%20of%20K%20Sum%20Pairs.py) | How could I improve that initial solution further without using a dictionary? |
| https://leetcode.com/problems/longest-palindromic-substring/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Longest%20Palindromic%20Substring.py) | --- | How could I solve this differently? |
| https://leetcode.com/problems/valid-parentheses/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Valid%20Parentheses.py) | --- | How could I solve this problem differently? | 
| https://leetcode.com/problems/find-the-most-competitive-subsequence/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Find%20the%20Most%20Competitive%20Subsequence.py) | --- | Could I solve this as efficiently in another manner? |
| https://leetcode.com/problems/determine-if-two-strings-are-close/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Determine%20if%20Two%20Strings%20are%20Close.py) | --- | How could I solve this so as to minimize runtime. |
| https://leetcode.com/problems/merge-k-sorted-lists | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Hard/Merge%20K%20Sorted%20Lists.py) | [Improved Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Improved_Hard_Solutions/Mere%20K%20Sorted%20Lists.py) | My Initial Solution produces a TLE error on LeetCode. It passes only 132 of 133 test cases. My Improved Solution uses a heap. How could I solve this in another way? |
| https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/commit/82f2a9176a223e3ba482502878feac9e019e171a) | --- | How could I solve this problem so as to minimize space and time complexity? |
| https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Concatenation%20of%20Consecutive%20Binary%20Numbers.py) | --- | How could I write this so as to improve runtime? To reduce its memory footprint? |
| https://leetcode.com/problems/smallest-string-with-a-given-numeric-value | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Smallest%20String%20With%20a%20Given%20Numeric%20Value.py) | --- | My initial solution isn't particularly efficient. How could I improve both space and time complexity? | 
| https://leetcode.com/problems/number-of-1-bits/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Number%20of%201%20Bits.py) | --- | When I initially attempted this problem, I cast n to a string as s = str(n). I encountered unexpected behavior: namely, only the rightmost cluster of ones was "sticking." So, for example, n = 110010001011 became s = '11'. I assume this was an error in the platform. I'd like to understand why this was happening. |
| https://leetcode.com/problems/linked-list-cycle | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Linked%20List%20Cycle.py) | --- | This solution isn't particularly elegant. Upon a rewrite, I should like to improve the runtime. |
| https://leetcode.com/problems/simplify-path | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Simplify%20Path.py) | --- | Approaching this problem in the way that I've done here (by using a stack) is straightforwardly correct. But what other approach, if any, might I take? |
| https://leetcode.com/problems/shortest-distance-to-a-character/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Shortest%20Distance%20to%20a%20Character.py) | --- | What's another algorithm I could use to solve this? |
| https://leetcode.com/problems/peeking-iterator/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Peeking%20Iterator.py) | --- | How could I write this differently? |
| https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Number%20of%20Steps%20to%20Reduce%20a%20Number%20to%20Zero.py) | --- | How could I reduce runtime? Reduce memory usage? |
| https://leetcode.com/problems/letter-case-permutation/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Letter%20Case%20Permutation.py) | --- | I relied entirely on "product". How would I write this from scrtach without relying upon inbuilt methods? |
| https://leetcode.com/problems/container-with-most-water/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Medium/Container%20With%20Most%20Water.py) | --- | How could I solve this another way? |
| https://leetcode.com/problems/remove-palindromic-subsequences/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Remove%20Palindromic%20Subsequences.py) | --- | It would be good to solve a modified version of the problem wherein one could only delete subarrays instead of being able to delete subsequences. |
| https://leetcode.com/problems/verifying-an-alien-dictionary/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Verifying%20an%20Alien%20Dictionary.py) | --- | It would be worthwhile to solve this without leveraging the built-in functions I'm using here (zip, ziplongest at least). | 
| https://leetcode.com/problems/fibonacci-number/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/fibonacci_number.py) | I've implemented another solution, which is worse than my initial solution. It is inlcuded as a comment at the end of the Initial Solution link. | Runtime: 28 ms, faster than 84.54% of Python3 online submissions for Fibonacci Number. Memory Usage: 14.2 MB, less than 41.72% of Python3 online submissions for Fibonacci Number. | 
| https://leetcode.com/problems/fibonacci-number/ | [Initial Solution]https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Swift/Easy/two_sum.swift(https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/n-th-tribonacci-number.py) | [Improved Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Improved_Easy_Solutions/n-th-tribonacci-number.py) | Runtime: 24 ms, faster than 94.50% of Python3 online submissions for N-th Tribonacci Number. Memory Usage: 14.3 MB, less than 45.27% of Python3 online submissions for N-th Tribonacci Number.| 
| https://leetcode.com/problems/combine-two-tables | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/db/Easy/combine-two-tables) | --- | Runtime: 302 ms, faster than 94.80% of MySQL online submissions for Combine Two Tables. Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables. | 
| https://leetcode.com/problems/two-sum/ | [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Swift/Easy/two_sum.swift) | --- | Runtime: Runtime: 58 ms Memory Usage: 14.4 MB. | 
|https://leetcode.com/problems/palindrome-number/| [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Swift/Easy/palindrome_number.swift) | --- | Runtime: 121 ms, faster than 5.29% of Swift online submissions for Palindrome Number. Memory Usage: 14.5 MB, less than 7.20% of Swift online submissions for Palindrome Number. | 
|https://leetcode.com/problems/plus-one/| [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Swift/Easy/plusOne.swift) | --- | ERROR: process exited with signal SIGILL. // I believe this _is_ a solution. TO DO: 1) test with Xcode and determine whether this a limitation or bug in LeetCode's platform. 2) Write another, different solution that succeeds on LeetCode's platform. | 
|https://leetcode.com/problems/longest-common-prefix| [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/Longest_Common_Prefix.py) | --- | Runtime: 45 ms, faster than 57.52% of Python3 online submissions for Longest Common Prefix.Memory Usage: 14 MB, less than 50.87% of Python3 online submissions for Longest Common Prefix. | 
|https://leetcode.com/problems/median-of-two-sorted-arrays| [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Hard/median_of_two_sorted_arrays.py) | --- | Runtime: 93 ms, faster than 91.24% of Python3 online submissions for Median of Two Sorted Arrays. Memory Usage: 14.2 MB, less than 68.93% of Python3 online submissions for Median of Two Sorted Arrays. | 
|https://leetcode.com/problems/min-cost-climbing-stairs/| [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/min_cost_climbing_stairs.py) | --- | Runtime: 87 ms Memory Usage: 14 MB |
|https://leetcode.com/problems/running-sum-of-1d-array/| [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/running_sum_of_1d_array.py) | --- | Runtime: 71 ms, faster than 35.88% of Python3 online submissions for Running Sum of 1d Array. Memory Usage: 14.2 MB, less than 27.31% of Python3 online submissions for Running Sum of 1d Array. |
|https://leetcode.com/problems/find-pivot-index/| [Initial Solution](https://github.com/lukemshannonhill/LeetCode_Daily_Problem_Solutions/blob/master/Easy/find_pivot_index.py) | --- | Runtime: 324 ms, faster than 16.72% of Python3 online submissions for Find Pivot Index. Memory Usage: 15.3 MB, less than 48.84% of Python3 online submissions for Find Pivot Index. |
