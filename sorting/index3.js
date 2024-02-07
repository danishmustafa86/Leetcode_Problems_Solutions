// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
// Example 1:
// Input: nums = [1,2,3,1]
// Output: true
// Example 2:
// Input: nums = [1,2,3,4]
// Output: false
function containsDuplicate(nums) {
    var n1 = 0;
    for (var i = 0; i < nums.length; i++) {
        // let num2:number=nums[i]
        for (var j = 1; j < nums.length; i++) {
            if (n1[i] == n1[j]) {
                return true;
            }
        }
    }
    return false;
}
;
console.log([1, 2, 3, 1]);
