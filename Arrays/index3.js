function shufflong(nums, n) {
    var result = [];
    for (var index = 0; index < n; index++) {
        var element = nums[index];
        result.push(nums[index]);
        result.push(nums[index + n]);
    }
    return result;
}
console.log(shufflong([1, 2, 3, 4, 4, 3, 2, 1], 4));
