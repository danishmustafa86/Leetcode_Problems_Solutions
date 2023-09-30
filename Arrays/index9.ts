function createTargetArray(nums: number[], index: number[]): number[] {
    let target:number[]=[]
    for(let i=0;i<nums.length;i++){
        target.splice(index[i],1,nums[i])
    }
    console.log(nums.length);
     return target
 };
 console.log(createTargetArray([1,2,4,5],[3,4,1,2]));
 