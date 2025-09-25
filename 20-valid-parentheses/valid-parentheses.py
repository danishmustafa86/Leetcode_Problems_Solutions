class Solution:
    def isValid(self, s: str) -> bool:
        st = "([{"
        end = ")]}"
        stack = []

        for i in s:
            if i in st:
                # If it's an opening bracket, push onto the stack
                stack.append(i)
            elif i in end:
                # Check if stack is not empty and the last item matches the corresponding opening bracket
                if not stack or stack[-1] != st[end.index(i)]:
                    return False
                else:
                    # Pop the matching opening bracket
                    stack.pop()

        # Ensure stack is empty at the end, meaning all brackets were matched
        return len(stack) == 0
