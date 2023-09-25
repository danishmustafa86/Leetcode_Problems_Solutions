// Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

// Return the running sum of nums.
function runningSum(nums: number[]):number[] {
    let newarry:number[]=[]
     let sum:number=0
  nums.map((elm)=>{
 sum=sum+elm
 newarry.push(sum)
  })
  return newarry
     };
     console.log(runningSum([1,2,3,4]));
     










