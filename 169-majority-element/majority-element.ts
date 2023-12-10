function majorityElement(nums: number[]): number {
   let sortedArray=nums.sort()
    return sortedArray[Math.floor(sortedArray.length / 2)]
};