// Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
// Example 1:
// Input: nums1 = [1,2,2,1], nums2 = [2,2]
// Output: [2]
// Example 2:
// Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// Output: [9,4]
// Explanation: [4,9] is also accepted.

function intersection(nums1: number[], nums2: number[]) {
    let arr:number[]=[]
    for (let i = 0; i < nums1.length; i++) {
        if (nums2.includes(nums1[i])) {
            arr.push(nums2[i])
        }
    }
    for (let j = 0; j < arr.length; j++) {
        for (let k = 0; k < arr.length; k++) {
            if (j !== k && arr[j] === arr[k]) { 
                arr.splice(j--, 1)
        }
    }
}
return arr
}
console.log(intersection([4,9,5],[9,4,9,8,4]));


// for (let m = 0; m < array.length; m++) {    
// }



// function missingNumber(nums: number[]) {
//     nums=nums.sort()
//     let n=nums.length
//     let n1:number=0
//     for(let i=0;i<=n;i++){
//         if(!nums.includes(i)){
//            return i
//         }
//     }
    
// };
// console.log(missingNumber([3,0,1]));
