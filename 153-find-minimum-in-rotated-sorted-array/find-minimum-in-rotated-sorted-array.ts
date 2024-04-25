function findMin(nums: number[]): number {
    nums = nums.sort((a,b) => a-b)
    return nums[0]
};