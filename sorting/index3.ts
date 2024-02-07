// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
// Example 1:
// Input: nums = [1,2,3,1]
// Output: true
// Example 2:
// Input: nums = [1,2,3,4]
// Output: false

function containsDuplicate(nums: number[]): boolean {
    let n1:number=0
for (let i = 0; i < nums.length; i++) {
    let num2:number=nums[i]
    for (let j = 1; j < nums.length; i++) {
        if (num2==n1[j]) {
          return true  
        }
    }
}
return false
};
console.log([1,0,3,2,6,9,2,5]);
