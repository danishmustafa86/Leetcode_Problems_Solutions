function productExceptSelf(nums: number[]): number[] {
    let n:number=nums.length
    const left:number[]=[]
    const right:number[]=[]
    const output:number[]=[]
    // calculate left multiplication
    left[0]=1
    for (let i=1;i<n;i++){
        left[i]=left[i-1]*nums[i-1]
    }
    // calculate right multiplication
    right[n-1]=1
    for (let i=n-2;i>=0;i--){
        right[i]=right[i+1]*nums[i+1]
    }
    // calculate output/
    for (let i=0;i<n;i++){
        output[i]=left[i]*right[i]
    }
    return output
}



// function productExceptSelf(nums: number[]): number[] {
//     const n = nums.length;
//     const left: number[] = [];
//     const right: number[] = [];
//     const output: number[] = [];

//     // Calculate left products
//     left[0] = 1;
//     for (let i = 1; i < n; i++) {
//         left[i] = left[i - 1] * nums[i - 1];
//     }

//     // Calculate right products
//     right[n - 1] = 1;
//     for (let i = n - 2; i >= 0; i--) {
//         right[i] = right[i + 1] * nums[i + 1];
//     }

//     // Calculate output
//     for (let i = 0; i < n; i++) {
//         output[i] = left[i] * right[i];
//     }

//     return output;
// }








// My this solution is true but its takes a problem only due to time complexity

// function productExceptSelf(nums: number[]): number[] {
//     let arr=[]
//     let product=1
//     for(let i=0;i<nums.length;i++){
//         for(let j=0;j<nums.length;j++){
//             if(i!=j){
//                 product=product*nums[j]
//             }
//         }
//         arr.push(product)
//         product=1
//     }
//     return arr
// };








        // nums.splice(i,1)
        // product=nums.reduce((accumulator,currentvalue) => accumulator*currentvalue)
        // arr.push(product)