function removeElement(nums: number[], val: number): number {
    
    for(let i=0;i<nums.length;i++){
        if(nums[i]===val){
            nums.splice(i,1)
            i--
        }
    }
    let k=nums.length
    return k
};