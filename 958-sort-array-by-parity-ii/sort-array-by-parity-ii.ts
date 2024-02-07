function sortArrayByParityII(nums: number[]): number[] {
    let odd:number[]=[]
    let even:number[]=[]
    let ans:number[]=[]
    for (let i=0;i<nums.length;i++){
        if(nums[i]%2==0){
            even.push(nums[i])
        }
        if(nums[i]%2==1){
            odd.push(nums[i])
        }
    }
    for (let j=0;j<odd.length;j++){
        ans.push(even[j])
        ans.push(odd[j])
    }
    return ans
};