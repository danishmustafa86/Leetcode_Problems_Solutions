function majorityElement(nums: number[]): number {
    return nums.sort()[Math.floor(nums.length / 2)]
};