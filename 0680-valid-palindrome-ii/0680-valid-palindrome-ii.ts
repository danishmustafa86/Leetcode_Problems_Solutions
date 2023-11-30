function validPalindrome(s: string): boolean {
    let left: number = 0;
    let right: number = s.length - 1;

    while (left < right) {
        if (s[left] !== s[right]) {
            // Try skipping either the character at the left or right index
            return (
                isPalindrome(s, left + 1, right) || isPalindrome(s, left, right - 1)
            );
        }

        left++;
        right--;
    }

    return true;
}

function isPalindrome(s: string, start: number, end: number): boolean {
    while (start < end) {
        if (s[start] !== s[end]) {
            return false;
        }
        start++;
        end--;
    }
    return true;
}
