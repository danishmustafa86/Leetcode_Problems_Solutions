//  function merge(nums1: number[], m: number, nums2: number[], n: number) {
//    for (let i=m+n-1;i>=0;i--) {
//     if (nums1[i]==0) {
//         nums1.splice(i, 1);    }
//    }
//    console.log(nums1);
   
//    nums1=nums1.concat(nums2)
//    nums1=nums1.sort()
//   return nums1
//    };


/**
 Do not return anything, modify nums1 in-place instead.
 */

function merge(nums1: number[], m: number, nums2: number[], n: number): void { 
nums1.splice(m,n,...nums2)
nums1.sort((a,b)=>a-b)
};
/**
 Do not return anything, modify nums1 in-place instead.
 */

// function merge(nums1: number[], m: number, nums2: number[], n: number): void { 
//   nums1.splice(m,n,...nums2)
//   nums1.sort((a,b)=>a-b)
// };