// function longestSubarray(nums: number[]): number {
//     if(nums.length==1) return 0
//     let n=1
//     let arr=[]
//     for(let i=0;i<nums.length;i++){
//         nums.splice(i,1)
//         for(let j=0;j<nums.length-1;j++){
//             if(nums[j]==1 && nums[j]==nums[j+1]){
//                 n++
//             }else if (nums[j]!=nums[j+1]){
//                 arr.push(n)
//                 n=0
//             }
//         }
//     }
//     return Math.max(...arr)
// };
function longestSubarray(nums: number[]): number {
    let maxLen = 0;
    let currentLen = 0;
    let hasZero = false;
    let lastZeroIndex = -1;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            currentLen++;
        } else {
            if (hasZero) {
                maxLen = Math.max(maxLen, currentLen);
                currentLen = i - lastZeroIndex - 1;
                lastZeroIndex = i;
            } else {
                hasZero = true;
                lastZeroIndex = i;
            }
        }
    }

    maxLen = Math.max(maxLen, currentLen);

    return hasZero ? maxLen : currentLen - 1;
}
