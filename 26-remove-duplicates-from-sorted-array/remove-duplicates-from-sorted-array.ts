function removeDuplicates(nums: number[]): number {

    let authIndex = 1;
  
    for (let i = 1; i < nums.length; i++) {
      if (nums[i] !== nums[i - 1]) {
        nums[authIndex] = nums[i];
        authIndex++;
      }
    }
  
    return authIndex;
  }
  