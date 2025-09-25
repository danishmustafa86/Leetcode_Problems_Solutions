class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Create a set for fast lookup of dictionary words
        word_set = set(dictionary)
        
        # Initialize dp array, where dp[i] is the minimum number of extra characters
        # for the substring s[0:i]
        dp = [0] * (len(s) + 1)
        
        # Loop through all possible lengths of the substring
        for i in range(1, len(s) + 1):
            # By default, assume the entire substring s[0:i] is made up of extra characters
            dp[i] = dp[i-1] + 1
            
            # Check all possible starting points of substrings ending at index i-1
            for word in word_set:
                word_len = len(word)
                if i >= word_len and s[i-word_len:i] == word:
                    dp[i] = min(dp[i], dp[i-word_len])
        
        # The result is stored in dp[len(s)], which represents the entire string
        return dp[len(s)]
