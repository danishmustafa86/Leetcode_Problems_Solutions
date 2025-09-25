function removeElement(nums: number[], val: number): number {
    let slow = 0, i = 0;
    while (i<nums.length) {
        if(nums[i] !=val){
            nums[slow]=nums[i]
            slow+=1
        }i++
    }
    // let k=nums.length
    return slow
};