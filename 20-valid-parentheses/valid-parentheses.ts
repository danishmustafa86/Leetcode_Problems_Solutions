function isValid(s: string): boolean {
    // Create an empty array to serve as a stack for brackets
    const stack: string[] = [];

    // Define sets of opening and closing brackets
    const openingBrackets = '({[';
    const closingBrackets = ')}]';

    // Iterate through each character in the input string
    for (let i = 0; i < s.length; i++) {
        // Get the current bracket
        const currentBracket = s[i];

        // Check if the current bracket is an opening bracket
        if (openingBrackets.includes(currentBracket)) {
            // If it is, push it onto the stack
            stack.push(currentBracket);
        } else {
            // If it's a closing bracket, pop the last opened bracket from the stack
            const lastOpenedBracket = stack.pop();

            // Check if there is a corresponding opening bracket
            if (!lastOpenedBracket || openingBrackets.indexOf(lastOpenedBracket) !== closingBrackets.indexOf(currentBracket)) {
                // If not, return false (invalid)
                return false;
            }
        }
    }

    // After the loop, check if there are any unmatched opening brackets left in the stack
    return stack.length === 0;
}

// Test cases
console.log(isValid("()"));        // Output: true
console.log(isValid("()[]{}"));    // Output: true
console.log(isValid("(]"));         // Output: false
