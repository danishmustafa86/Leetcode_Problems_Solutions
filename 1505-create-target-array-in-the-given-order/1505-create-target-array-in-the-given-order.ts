function createTargetArray(nums: number[], index: number[]): number[] {
   let targetArray:number[]=[]
   for(let i=0;i<nums.length;i++){
       targetArray.splice(index[i],0,nums[i])
   }
    return targetArray
};