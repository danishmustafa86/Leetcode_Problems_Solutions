function removeElement(nums: number[], val: number): number {
    let slow=0
    for(let i=0;i<nums.length;i++){
        if(nums[i] !=val){
            nums[slow]=nums[i]
            slow+=1
        }
    }
    // let k=nums.length
    return slow
};