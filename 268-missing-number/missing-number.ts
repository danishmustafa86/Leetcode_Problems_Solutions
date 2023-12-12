function missingNumber(nums: number[]): number {
    nums=nums.sort()
    let n=nums.length
    let n1:number=0
    for(let i=0;i<=n;i++){
        if(!nums.includes(i)){
           return i
        }
    }
};
// function missingNumber(nums: number[]): number {
//     nums=nums.sort()
//     let n=nums.length
//     let n1:number=0
//     for(let i=0;i<=n;i++){
//         if(nums[i]!=(nums[i+1]-1)){
//             n1=nums[i]+1
//         }
//     }
//     return n1
// };