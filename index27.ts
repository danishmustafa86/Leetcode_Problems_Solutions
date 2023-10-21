// function removeDuplicates(nums: number[]):number {
// let authindex:number=1
// for (let i = 0; i < nums.length ; i++) {
//     if (nums[i]!=nums[i-1]) {
//         nums[authindex]=nums[i]
//         authindex++
//     }
// }

// return authindex
// };


function removeDuplicates(nums: number[]): number {

    let authIndex = 1;
  
    // Iterate through the array starting from the second element (index 1).
    for (let i = 1; i < nums.length; i++) {
      // Check if the current element is different from the previous one (it's unique).
      if (nums[i] !== nums[i - 1]) {
          // Place the unique element at the authIndex and increment the pointer.
        nums[authIndex] = nums[i];
        authIndex++;
      }
    }
  
    // The value of authIndex represents the count of unique elements.
    return authIndex;
  }
  
          console.log(removeDuplicates([0,0,3,1,5,2,3,3,4]));