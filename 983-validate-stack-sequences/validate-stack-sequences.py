class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        stack = []
        for s in pushed:
            stack.append(s)
            while i < len(pushed) and stack and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        
        return len(stack) == 0