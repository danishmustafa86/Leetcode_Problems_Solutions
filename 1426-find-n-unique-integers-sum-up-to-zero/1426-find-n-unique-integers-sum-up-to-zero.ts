// function sumZero(n: number) {
//     let arr: number[] = new Array(n);
// if (n%2==0) {
//     for (let i = 0; i < n-1; ) {
//         arr[i]=i+1
//         arr[i+1]=-(i+1)
//     }
// } else {
//     for (let i = 0; i < n-1; i=i+2) {
//         arr[i]=i+1
//         arr[i+1]=-(i+1)
//     }
//     arr[n-1]=0  
// }
// return arr
// };
function sumZero(n: number) {
    let arr: number[] =[]
if (n%2==0) {
    for (let i = 1; i < n;i=i+2 ) {
        arr.push(i)
        arr.push(-i)      
    }
} else {
    for (let i = 1; i < n; i=i+2) {
        arr.push(i)
        arr.push(-i)
    }
    arr[n-1]=0  
}
return arr

};
// console.log(sumZero(4));
