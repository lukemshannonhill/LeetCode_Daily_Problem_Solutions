// https://leetcode.com/problems/plus-one/

class Solution {
    func plusOne(_ digits: [Int]) -> [Int] {
        
        var dig = digits
        
        var z = dig.last!
        
        if z < 9 {
            z += 1
            dig.removeLast()
            dig.append(z)
            return dig
        }
        
        var total = 0
        var l = digits.count
        
        var b:[Int] = []
        
        for e in digits.reversed() {
            b.append(e)
        }
        
        var temp = l
        var tens = 1
        
         while temp != 1 {
                tens = tens * 10
                temp -= 1 
                }
        
        while l > 0 {
            
            let d = b.last!
            b = b.dropLast()
            
            let add = tens * d
            total = total + add
            tens = tens/10
            l -= 1
        
        }
        
        total += 1
        let s = String(total)
        let returnVal = s.map { char -> Int in 
                              if let intVal = Int(String(char)){
                                  return intVal
                              }
                                    return 0
        }
        
        return returnVal
    }
}
