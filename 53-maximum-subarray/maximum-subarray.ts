function maxSubArray(nums: number[]) {
    let maxarray:number=-76996985346
    let minsum:number=0
    for (let i = 0; i < nums.length; i++) {
        minsum=minsum+nums[i]
if (minsum>maxarray) {
    maxarray=minsum
}
if (minsum<0) {
    minsum=0
}        
    }
    return maxarray
};
