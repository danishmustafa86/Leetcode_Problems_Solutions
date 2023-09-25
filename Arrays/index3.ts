function shufflong(nums:number[],n:number):number[] {
    let result:number[]=[]
    for (let index = 0; index < n; index++) {
        const element = nums[index];
result.push(nums[index])
result.push(nums[index+n])
        
    }
   return result 
}

console.log(shufflong([1,2,3,4,4,3,2,1],4));


