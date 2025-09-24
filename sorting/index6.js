// Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
// Example 1:
// Input: nums = [3,2,1]
// Output: 1
// Explanation:
// The first distinct maximum is 3.
// The second distinct maximum is 2.
// The third distinct maximum is 1.
// function thirdMax(nums: number[]): number {
//     let n1: number = 0
//     let n2: number[] = []
//     nums = nums.sort((a, b) => a - b)
//     if (nums.length > 2) {
//         nums.splice(nums.indexOf(Math.max(...nums)), 1);
//         nums.splice(nums.indexOf(Math.max(...nums)), 1);
//     n1 = Math.max(...nums)
//     }
//     else {
//         n1 = Math.max(...nums)
//     }
//     return n1
// };
function thirdMax(nums) {
    var set = new Set(nums);
    var max1 = Math.max.apply(Math, set);
    if (nums.length < 3)
        return max1;
    set.delete(max1);
    var max2 = Math.max.apply(Math, set);
    set.delete(max2);
    var max3 = Math.max.apply(Math, set);
    return max3;
}
;
console.log(thirdMax([3, 2, 1]));
console.log(thirdMax([2, 2, 3, 1]));
