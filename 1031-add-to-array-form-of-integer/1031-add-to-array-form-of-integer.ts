function addToArrayForm(num: number[], k: number) {
    let list: number[] = [];
    for (let i = num.length - 1; i >= 0 || k > 0; i--) {
        if (i >= 0) {
            list.unshift((num[i] + k) % 10);
            k = Math.floor((num[i] + k) / 10);
        } else {
            list.unshift(k % 10);
            k = Math.floor(k / 10); // Use integer division here
        }
    }
    return list;
}

// Example usage:
const num = [1, 2, 0, 0];
const k = 34;
const result = addToArrayForm(num, k);
console.log(result); // Output: [1, 2, 3, 4]
