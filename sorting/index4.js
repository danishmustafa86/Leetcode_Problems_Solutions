// Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
// Example 1:
// Input: nums1 = [1,2,2,1], nums2 = [2,2]
// Output: [2]
// Example 2:
// Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// Output: [9,4]
// Explanation: [4,9] is also accepted.
// function intersection(nums1: number[], nums2: number[]): number[] {
//     let arr:number[]=[]
//     for (let i = 0; i < nums1.length; i++) {
//         if (nums2.includes(nums1[i])) {
//             arr.push(nums2[i])
//         }
//     }
//     return arr
// };
// console.log(intersection([4,9,5],[9,4,9,8,4]));
function missingNumber(nums) {
    nums = nums.sort();
    var n = nums.length;
    var n1 = 0;
    for (var i = 0; i <= n; i++) {
        if (!nums.includes(i)) {
            return i;
        }
    }
}
;
console.log(missingNumber([3, 0, 1]));
