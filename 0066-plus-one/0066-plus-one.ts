function plusOne(digits: number[]): number[] {
    for (let i = digits.length - 1; i >= 0; i--) {
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
        return [1, ...digits];
    }

    // If the original number didn't have all 9s, return the updated array.
    return digits;
}
