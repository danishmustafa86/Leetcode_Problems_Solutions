function longestConsecutive(nums: number[]) {
    if(nums.length==0) return 0
    let numSet=new Set(nums)
    let max=0
    for(let num of nums){
        if(!numSet.has(num-1)){
            let current=num
            let currentValue=1
            while(numSet.has(current+1)){
                current++
                currentValue++
            }
            max=Math.max(max,currentValue)
        }
    }
    return max

}



































// function longestConsecutive(nums: number[]) {
//     if(nums.length==0) return 0
//      let numSet = new Set(nums);
//    let arr = nums.sort((a, b) => a - b);   
//    let n=1
//      for(let i=0;i<nums.length-1;i++){
//         if(nums[i]+1==nums[i+1]){
//             n++
//         }
//     }
//     return n
// };


    // let arr = nums.sort((a, b) => a - b);

// function longestConsecutive(nums: number[]) {
//     let n = 0;
//     let min
//     for(let i=0; i<nums.length;i++){
//         min=nums[i]
//         for(let j=i+1;j<nums.length;j++){
//             if(min>nums[j]){
//                 min=nums[j]
//                 nums[i]=nums[j]
//                 nums[j]=nums[i]
//             }
//         }
//     }
//     for (let i = 0; i < nums.length - 1; i++) {
//         if (nums[i] + 1 === nums[i + 1]) {
//             n++;
//         }
//     }
//     return n;
// }











// function sorting(sort:number[]){
//     let min
//     for(let i=0; i<sort.length;i++){
//         min=sort[i]
//         for(let j=i+1;j<sort.length;j++){
//             if(min>sort[j]){
//                 min=sort[j]
//                 sort[i]=sort[j]
//                 sort[j]=sort[i]
//             }
//         }
//     }
//     return sort
// }
