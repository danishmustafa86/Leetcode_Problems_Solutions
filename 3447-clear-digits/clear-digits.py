class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i].isalpha():
                stack.append(s[i])
            else:
                stack.pop()
        return "".join(stack)


