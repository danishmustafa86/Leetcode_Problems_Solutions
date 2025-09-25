class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:  # Odd length strings cannot be valid
            return False
        
        open_count = 0  # To track open parentheses
        unlocked_count = 0  # To track unlocked characters
        
        # Left to right pass
        for i in range(len(s)):
            if locked[i] == '0':  # Unlocked character
                unlocked_count += 1
            elif s[i] == '(':
                open_count += 1
            else:  # s[i] == ')'
                if open_count > 0:  # Balance with an open parenthesis
                    open_count -= 1
                elif unlocked_count > 0:  # Use an unlocked character
                    unlocked_count -= 1
                else:  # No way to balance this ')'
                    return False
        
        # Reset counts for right to left pass
        close_count = 0  # To track close parentheses
        unlocked_count = 0  # Reset unlocked characters
        
        # Right to left pass
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0':  # Unlocked character
                unlocked_count += 1
            elif s[i] == ')':
                close_count += 1
            else:  # s[i] == '('
                if close_count > 0:  # Balance with a close parenthesis
                    close_count -= 1
                elif unlocked_count > 0:  # Use an unlocked character
                    unlocked_count -= 1
                else:  # No way to balance this '('
                    return False
        
        return True
