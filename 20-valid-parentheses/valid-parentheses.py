class Solution:
    def isValid(self, s: str) -> bool:
        st1 = "([{"
        st2 = ")]}"
        stk = []
        match_brackets = { ")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in st1:
                stk.append(i)
            elif i in st2:
                if not stk or stk[-1] != match_brackets[i]:
                    return False
                stk.pop()
        return len(stk) == 0
                    

        # st1 = "([{"
        # st2 = ")]}"
        # matching_brackets = {')': '(', ']': '[', '}': '{'}
        # stack = []
        
        # for i in s:
        #     if i in st1:  # If it's an opening bracket, push to stack
        #         stack.append(i)
        #     elif i in st2:  # If it's a closing bracket
        #         # Check if stack is empty or top of stack doesn't match
        #         if not stack or stack[-1] != matching_brackets[i]:
        #             return False
        #         stack.pop()  # Pop the matching opening bracket
        
        # # Check if the stack is empty (all brackets matched)
        # return len(stack) == 0
