function majorityElement(nums: number[]): number {
    let n : number = nums.length , carry : number = 1 , element: number = nums[0]

    for(let i =1;i<n;i++){
        if(element === nums[i]){
            carry++
        }else{
            carry--
        }
        if(carry < 0){
            carry++
            element = nums[i]
        }
    }
    return element
};