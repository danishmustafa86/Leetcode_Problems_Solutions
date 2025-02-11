class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= len(part) and ''.join(stack[-len(part):]) == part:
                j = len(part) 
                while j > 0:
                    stack.pop()
                    j -= 1


        return "".join(stack)