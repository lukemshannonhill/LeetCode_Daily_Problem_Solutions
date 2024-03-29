// https://leetcode.com/problems/two-sum/

class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var actualSearchNumber:Int;
        for i in 0..<nums.count-1 {
            actualSearchNumber = target - nums[i];
            for j in i+1..<nums.count {
                if nums[j] == actualSearchNumber {
                    return [i, j];
                }
            }
        }
        return [-1, -1];
    }
}
