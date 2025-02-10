class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        lower_letters = [ chr(i) for i in range(ord('a'), ord("z") + 1)]
        for i in range(len(s)):
            if s[i] not in lower_letters:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)


