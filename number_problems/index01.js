// Given an integer number n, return the difference between the product of its digits and the sum of its digits.
// Example 1:
// Input: n = 234
// Output: 15 
// Explanation: 
// Product of digits = 2 * 3 * 4 = 24 
// Sum of digits = 2 + 3 + 4 = 9 
// Result = 24 - 9 = 15
function subtractProductAndSum(n) {
    var st = n.toString();
    var product = 1;
    var sum = 0;
    for (var i = 0; i < st.length; i++) {
        var n2 = parseInt(st[i]);
        product = product * n2;
        sum = sum + n2;
        console.log(n2);
    }
    console.log(product);
    console.log(sum);
    return product - sum;
}
;
console.log(subtractProductAndSum(2783));
