// https://leetcode.com/problems/palindrome-number/

class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        
        var y = String(x)
        
        while y != ""{
                    
            if y.count == 1 {
                return true
            }

            var templast = y.removeLast()

            var a = String(y.reversed())
            var tempfirst = a.removeLast()

                    
            y = String(a.reversed())

            if templast != tempfirst{

                return false
            }
                    
            if templast == tempfirst {
                if y.count == 0 {
                    return true
                }
            }
        }
    return true
    }
}
