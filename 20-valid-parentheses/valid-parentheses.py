class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hsh = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for i in s:
            if i in hsh:
                if stack and stack[-1] == hsh[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0




















        
# class Solution:
#     def isValid(self, s: str) -> bool:
#         st1 = "([{"
#         st2 = ")]}"
#         stk = []
#         match_brackets = { ")":"(", "]":"[", "}":"{"}
#         for i in s:
#             if i in st1:
#                 stk.append(i)
#             elif i in st2:
#                 if not stk or stk[-1] != match_brackets[i]:
#                     return False
#                 stk.pop()
#         return len(stk) == 0
                    
