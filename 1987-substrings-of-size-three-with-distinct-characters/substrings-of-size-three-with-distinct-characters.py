class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        if len(s) < 3:
            return 0
        
        stack = list(s[:3])
        
        # Check the first window
        if len(set(stack)) == 3:
            count += 1
        
        for i in range(3, len(s)):
            # Slide the window
            stack.pop(0)
            stack.append(s[i])
            
            # Check the current window
            if len(set(stack)) == 3:
                count += 1
                
        return count
