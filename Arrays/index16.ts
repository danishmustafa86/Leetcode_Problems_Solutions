function findNumbers(nums: number[],count=0) {
    for (let i = 0; i < nums.length; i++) {
      if (nums[i].toString().length%2==0) {
                  count++
      }
    }
    return count
      };
console.log(findNumbers([1,23,45,421]));

