// function searchInsert(nums: number[], target: number): number {
//   let k=0
//   for(let i=0;i<nums.length;i++){
//       if(nums[i]===target){
//           k=i
//           break;
//       } else if (target>nums[i]&&target<nums[i+1]){
//           k=i+1
//           break;
//       } else if (target>nums[nums.length-1]){
//           k=nums.length+1
//           break;
//       }else{
//           k=0
//       }
//     return k  
// };

function searchInsert(nums: number[], target: number): number {
    let k = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === target) {
            k = i;
            break; // Found the target, no need to continue
        } else if (target > nums[i] && (i === nums.length - 1 || target < nums[i + 1])) {
            k = i + 1; // Insertion point found
            break; // No need to continue, insertion point found
        } 
        // else if (target > nums[nums.length - 1]) {
        //     k = nums.length; // Insert at the end of the array
        //     break; // No need to continue, insertion point found
        // } 
        else {
            k = 0; // Insert at the beginning of the array
        }
    }
    return k;
}