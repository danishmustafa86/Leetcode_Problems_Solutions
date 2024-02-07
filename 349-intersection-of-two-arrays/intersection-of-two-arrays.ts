function intersection(nums1: number[], nums2: number[]): number[] {
    let arr:number[]=[]
    for (let i = 0; i < nums2.length; i++) {
            if (nums1.includes(nums2[i])&& !arr.includes(nums2[i])) {
                arr.push(nums2[i])
            }
        
    }
   return arr
};