// function twoSum(nums: number[], target: number): number[] {
// let array:number[]=[]
// for (let i=0;i<nums.length;i++){
//     for(let j=1;j<nums.length;j++){
//         if(i!=j&&nums[i]+nums[j]==target){
//             array.splice(0,2,i,j)
//         }
//     }
// }
// return array
// };
// console.log(twoSum([3,3],6));
function twoSum(nums, target) {
    var array = [];
    nums.map(function (e, i) {
        nums.map(function (l, j) {
            if (e != l && i + j == target) {
                array.splice(0, 2, e, l);
            }
        });
    });
    return array;
}
console.log(twoSum([3, 3], 6));
