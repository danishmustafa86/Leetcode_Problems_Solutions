function longestConsecutive(nums: number[]) {
    let n=0
    let arr=nums.sort()
    // for(let i=0;i<nums.length;i++){
    //     if(nums[i]+1==nums[i+1]){
    //         n++
    //     }
    // }
    return arr
};
console.log(longestConsecutive([100,4,200,1,3,2]))