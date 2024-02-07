// function missingNumber(nums: number[]): number {
//     nums=nums.sort()
//     let n=nums.length
//     let n1:number=0
//     for(let i=0;i<n;i++){
//         if(nums[i]!=(nums[i+1]-1)){
//             n1=nums[i]-1
//         }
//     }
//     return n1
// };





function missingNumber(nums: number[]): number {
    nums = nums.sort((a, b) => a - b); // Sorting in ascending order

    let n = nums.length;
    let n1: number = 0;
 if (nums[0] !== 0) {
        return 0;
    }

    // Check if n is missing at the end
    if (nums[n - 1] !== n) {
        return n;
    }
    for (let i = 0; i < n; i++) {
        if (nums[i] !== i) {
            n1 = i;
            break;
        }
    }

    // If no missing number is found at the end
    if (n1 === 0) {
        n1 = n;
    }

    return n1;
}




// function missingNumber(nums: number[]): number {
//     nums = nums.sort();
//     let n = nums.length;
//     let n1: number = 0;

//     for (let i = 0; i < n; i++) {
//         if (nums[i] !== i) {
//             n1 =i;
//         }
//     }
//     if(n1===0){
//     n1=n
//         }
//     return n1;
// }



// function missingNumber(nums: number[]): number {
//     nums=nums.sort()
//     let n=nums.length
//     let n1:number=0
//     for(let i=0;i<=n;i++){
//         if(!nums.includes(i)){
//            return i
//         }
//     }
// };