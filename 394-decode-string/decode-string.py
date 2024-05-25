class Solution:
    def decodeString(self, s: str) -> str:
        stack =[]
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                # find the string
                X = ""
                while (stack[-1].isalpha() == True):
                    X = stack.pop() + X
                # dispose [
                stack.pop()
                n = ""
                # number
                while stack and (stack[-1].isdigit() == True):
                    n = stack.pop() + n
                if n == "":
                    n = 1
                else:
                    n = int (n)
                stack.append((X * n))
        print(stack)    

        return "".join(stack)
    
# https://leetcode.com/problems/decode-string/
        