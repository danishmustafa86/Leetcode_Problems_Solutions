function myAtoi(s: string): number {
    let i = 0;
    let sign = 1;
    let result = 0;

    // Step 1: Read in and ignore any leading whitespace.
    while (s[i] === ' ') {
        i++;
    }

    // Step 2: Check for sign.
    if (s[i] === '-' || s[i] === '+') {
        sign = s[i] === '-' ? -1 : 1;
        i++;
    }

    // Step 3: Read digits until non-digit or end of string.
    while (i < s.length && !isNaN(parseInt(s[i]))) {
        result = result * 10 + parseInt(s[i]);
        i++;
    }

    // Step 4: Apply sign.
    result *= sign;

    // Step 5: Clamp the result within the 32-bit signed integer range.
    const INT_MAX = Math.pow(2, 31) - 1;
    const INT_MIN = -Math.pow(2, 31);
    if (result > INT_MAX) {
        return INT_MAX;
    }
    if (result < INT_MIN) {
        return INT_MIN;
    }

    return result;
}
