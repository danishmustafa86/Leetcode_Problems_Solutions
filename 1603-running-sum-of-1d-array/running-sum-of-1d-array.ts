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
    