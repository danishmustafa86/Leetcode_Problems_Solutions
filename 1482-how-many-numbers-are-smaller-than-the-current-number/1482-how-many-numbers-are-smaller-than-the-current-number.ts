function smallerNumbersThanCurrent(nums: number[]): number[] {
let othernums=[]
for(let i=0;i<nums.length;i++){
let value=0
for(let j=0;j<nums.length;j++){
    if(nums[i]>nums[j]){
        value++
    }
}
        othernums.push(value)
}
return othernums
}