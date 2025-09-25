class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        n = len(s)
        max_vowels = 0
        current_count = 0
        
        # Initialize the first window
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        max_vowels = current_count
        
        # Slide the window across the string
        for i in range(k, n):
            if s[i - k] in vowels:
                current_count -= 1
            if s[i] in vowels:
                current_count += 1
            max_vowels = max(max_vowels, current_count)
        
        return max_vowels