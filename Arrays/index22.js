function sumZero(n) {
    var arr = [];
    if (n % 2 == 0) {
        for (var i = 1; i < n; i = i + 2) {
            arr.push(i);
            arr.push(-i);
            // arr[i]=i+1
            // arr[i+1]=-(i+1)
        }
    }
    else {
        for (var i = 1; i < n; i = i + 2) {
            arr.push(i);
            arr.push(-i);
            // arr[i]=i+1
            // arr[i+1]=-(i+1)
        }
        arr[n - 1] = 0;
    }
    return arr;
}
;
console.log(sumZero(4));
