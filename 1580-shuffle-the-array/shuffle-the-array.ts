function shuffle(nums:number[], n:number):number[] {
    let result:number[] = [];
for(let i=0;i<n;i++){
result.push(nums[i])
result.push(nums[n+i])

}
return result
}