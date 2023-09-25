// Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
// Return the running sum of nums.
function runningSum(nums) {
    var newarry = [];
    var sum = 0;
    nums.map(function (elm) {
        sum = sum + elm;
        newarry.push(sum);
    });
    return newarry;
}
;
console.log(runningSum([1, 2, 3, 4]));
