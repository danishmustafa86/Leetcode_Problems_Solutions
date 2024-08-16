class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0  # To store the maximum length of the valid substring
        left = 0  # Left pointer for the sliding window
        count = {}  # Dictionary to keep track of the frequency of characters in the current window
        max_count = 0  # Maximum frequency of a single character in the current window

        # Iterate through the string with the right pointer
        for right in range(len(s)):
            # Update the frequency of the current character
            count[s[right]] = count.get(s[right], 0) + 1
            
            # Update max_count to the highest frequency of any single character in the window
            max_count = max(max_count, count[s[right]])

            # If the current window size minus the max_count is greater than k,
            # it means we have more characters to replace than allowed, so we shrink the window
            if right - left + 1 - max_count > k:
                count[s[left]] -= 1  # Decrement the count of the character at the left pointer
                left += 1  # Move the left pointer to the right to shrink the window

            # Calculate the maximum length of a valid window seen so far
            max_len = max(max_len, right - left + 1)

        return max_len  # Return the maximum length found
