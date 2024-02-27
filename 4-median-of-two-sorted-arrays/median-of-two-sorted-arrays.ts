function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    let num=nums1.concat(nums2)
    num=num.sort((a,b) => a-b)
    if( num.length%2==1){
        return num[Math.floor(num.length/2)]
    } if(num.length%2==0){
        return (num[num.length/2]+num[num.length/2 -1])/2
    }
};