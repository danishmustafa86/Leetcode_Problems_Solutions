function intersect(nums1: number[], nums2: number[]): number[] {
  let arr:number[]=[]
  for(let i=0;i<nums1.length;i++) {
      if(nums2.includes(nums1[i])){
          
          arr.push(nums1[i])
        nums2.splice(nums2.indexOf(nums1[i]),1)
      }
  } 
  return arr
};