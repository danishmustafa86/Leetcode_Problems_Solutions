function plusOne(digits: number[]): number[] {
    const n = digits.length;
    let carry = 1; // Initialize carry to 1 to add 1 to the least significant digit.

    for (let i = n - 1; i >= 0; i--) {
        const sum = digits[i] + carry;
        digits[i] = sum % 10; // Update the current digit.
        carry = Math.floor(sum / 10); // Calculate carry for the next iteration.
    }

    // If there is a carry after the loop, add a new most significant digit.
    if (carry > 0) {
        digits.unshift(carry);
    }

    return digits;
}

console.log(plusOne([2, 3, 56, 4, 1, 5, 4, 0, 8, 0, 0, 7, 3, 1, 5, 6, 0, 0]));
