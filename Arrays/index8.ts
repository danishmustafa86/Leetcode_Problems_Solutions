function smallerNumbersThanCurrent(nums: number[]): number[] {
    let othernums:number[]=[]
    for(let i=0;i<nums.length;i++){
    for(let j=i+1;j<nums.length;j++){
        if(nums[i]>nums[j]){
    let value=0
            othernums.push(value+1)
        }
    }
    }
    return othernums
    }