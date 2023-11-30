function addToArrayForm(num: number[], k: number) {
    let i = num.length - 1;
    let list: number[] = [];
    while (i >= 0 || k > 0) {
        if (i >= 0) {
            list.unshift((num[i] + k) % 10);
            k = Math.floor((num[i] + k) / 10);
            i--;
        } else {
            list.unshift(k % 10);
            k = Math.floor(k / 10);
        }
    }
    return list;
}

// Example usage:
// const num = [1, 2, 0, 0];
// const k = 34;
// const result = addToArrayForm(num, k);
// console.log(result); // Output: [1, 2, 3, 4]
