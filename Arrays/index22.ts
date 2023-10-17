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
console.log(sumZero(4));
