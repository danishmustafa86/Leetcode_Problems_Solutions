var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
function plsOne(digits) {
    for (var i = digits.length - 1; i >= 0; i--) {
        if (digits[i] < 9) {
            // If the current digit is less than 9, we can increment it and return the array.
            digits[i] = digits[i] + 1;
            return digits;
        }
        // If the current digit is 9, set it to 0 and continue to the next (left) digit.
        digits[i] = 0;
    }
    // If we reach this point, it means all digits were 9 (e.g., 9, 99, 999, ...).
    // In this case, we need to add a new most significant digit '1' at the beginning of the array.
    if (digits[0] === 0) {
        return __spreadArray([1], digits, true);
    }
    // If the original number didn't have all 9s, return the updated array.
    return digits;
}
console.log(plsOne([2, 3, 56, 4, 1, 5, 4, 0, 8, 0, 0, 7, 3, 1, 5, 6, 0, 0]));
