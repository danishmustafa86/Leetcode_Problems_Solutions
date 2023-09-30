function createTargetArray(nums, index) {
    var target = [];
    for (var i = 0; i < nums.length; i++) {
        target.splice(index[i], 1, nums[i]);
    }
    console.log(nums.length);
    return target;
}
;
console.log(createTargetArray([1, 2, 4, 5], [3, 4, 1, 2]));
