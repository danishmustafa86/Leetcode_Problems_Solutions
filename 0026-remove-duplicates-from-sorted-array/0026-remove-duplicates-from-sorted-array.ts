function removeDuplicates(nums: number[]): number {
    // Check if the input array is empty
  //   if (nums.length === 0) {
  //     return 0; // If the array is empty, there are no duplicates to remove, so return 0.
  //   }
  
    // Initialize a pointer to keep track of the position where the next unique element should be placed.
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
  