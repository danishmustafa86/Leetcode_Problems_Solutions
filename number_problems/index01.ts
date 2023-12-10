// Given an integer number n, return the difference between the product of its digits and the sum of its digits.
// Example 1:
// Input: n = 234
// Output: 15 
// Explanation: 
// Product of digits = 2 * 3 * 4 = 24 
// Sum of digits = 2 + 3 + 4 = 9 
// Result = 24 - 9 = 15
// function subtractProductAndSum(n: number) {
// let st:string=n.toString()
// let product:number=1;
// let sum:number=0
//     for(let i=0;i<st.length;i++){
// let n2:number=parseInt(st[i])
// product=product*n2
// sum=sum+n2
// console.log(n2);


// }
// console.log(product);
// console.log(sum);
// return product-sum
// };
// console.log(subtractProductAndSum(2783));


function subtractProductAndSum(n: number) {
    let st: string = n.toString()
    let product: number = 1;
    let sum: number = 0
    for (let i = 0; i < st.length; i++) {
        let n2: number = parseInt(st[i])
        product = product * n2
        sum = sum + n2
    }
    return product - sum
};





