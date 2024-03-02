function sortedSquares(nums: number[]): number[] {
    for(let i=0;i<nums.length;i++){
        nums[i]=nums[i]*nums[i]
    }
    return nums.sort((a,b)=> a-b)
};