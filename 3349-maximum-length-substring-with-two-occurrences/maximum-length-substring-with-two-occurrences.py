class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        left = 0
        max_length = 0
        char_count = defaultdict(int)

        for right in range(len(s)):
            char_count[s[right]] += 1
            
            # If any character occurs more than twice, adjust the window
            while char_count[s[right]] > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            
            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length
