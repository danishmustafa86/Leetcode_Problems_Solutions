function singleNumber(nums: number[]): number {
nums.sort((a,b)=> a-b)
for (let i=0;i<nums.length;i+=2){
    if(nums[i]!=nums[i+1]){
        return nums[i]
    }}
    return -1
}




// function singleNumber(nums: number[]): number {
//     let result = 0;
//     for (let i = 0; i < nums.length; i++) {
//         result ^= nums[i];
//     }
//     return result;
// }


// function singleNumber(nums: number[]): number {
//   for ( let i=0;i<nums.length;i++){
//     for (let j=i+1;j<nums.length;j++){
//         if( nums[i]==nums[j]){
//             nums.splice(j,1)
//             nums.splice(i,1)
//             j--            
//             i--
//         }
//     }
//   }  
//   return nums[0]
// };