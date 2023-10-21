function maxSubArray(nums) {
    var maxarray = 0;
    var minsum = 0;
    for (var i = 0; i < nums.length; i++) {
        minsum = minsum + nums[i];
        if (minsum > maxarray) {
            maxarray = minsum;
        }
        if (minsum < 0) {
            minsum = 0;
        }
    }
    return maxarray;
}
;
console.log(maxSubArray([3, 9, -8, 3, -2, -9, 3, 3, 7]));
