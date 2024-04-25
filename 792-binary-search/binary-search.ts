function search(nums: number[], target: number): number {
    let index:number=-1
    for (let i=0; i < nums.length; i++){
        if(target==nums[i]){
            index=i
        }
    }
    return index
};