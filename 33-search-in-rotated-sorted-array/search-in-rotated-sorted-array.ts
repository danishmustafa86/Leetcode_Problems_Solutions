function search(nums: number[], target: number): number {
    for( let i=0; i<nums.length; i++){
        if (target == nums[i]){
            return i
        }
    }
    return -1
};