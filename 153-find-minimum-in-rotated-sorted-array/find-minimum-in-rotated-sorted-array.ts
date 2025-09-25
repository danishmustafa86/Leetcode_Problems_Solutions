function findMin(nums: number[]): number {
    let min = nums[0]
    for (let i=1; i<nums.length; i++){
        if (min > nums[i]){
            min = nums[i]
        }
    }
    return min

}


















    // nums = nums.sort((a,b) => a-b)
    // return nums[0]
