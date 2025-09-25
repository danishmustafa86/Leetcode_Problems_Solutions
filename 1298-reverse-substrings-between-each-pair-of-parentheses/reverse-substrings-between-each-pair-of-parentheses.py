class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        current_string = ""
        
        for char in s:
            if char == '(':
                stack.append(current_string)
                current_string = ""
            elif char == ')':
                current_string = stack.pop() + current_string[::-1]
            else:
                current_string += char
        
        return current_string
