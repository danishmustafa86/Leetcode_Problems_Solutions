function minSubArrayLen(target: number,nums: number[]): number {
  const n = nums.length;
  let low = 0;
  let sum = 0;
  let minLength = Number.MAX_SAFE_INTEGER;

  for (let high = 0; high < n; high++) {
    // add the current element to the sum
    sum += nums[high];

    // while the sum is greater than equal to the target
    // keep updating the minimum length and after that
    // remove the element from the left side i.e remove
    // the value of the low pointer to decrease the
    // sum even more as decreasing it will give us smaller
    // length only if the sum is gte to the target
    // but make sure the low pointer is within the boundary
    while (low <= high && sum >= target) {
      const currLength = high - low + 1;
      minLength = Math.min(minLength, currLength);
      sum -= nums[low];
      low++;
    }
  }
  // if our minLength is still MAX_INT
  // then the target does not exists
  // so directly return 0
  if (minLength === Number.MAX_SAFE_INTEGER) return 0;

  // otherwise return the minimum subarray length
  return minLength;
}