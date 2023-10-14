function buildArray(nums: number[]): number[] {
    let ans:number[] = [];
    for(let index: number = 0; index < nums.length; index++){
      ans.push(nums[nums[index]]);
    }
    return ans;
};