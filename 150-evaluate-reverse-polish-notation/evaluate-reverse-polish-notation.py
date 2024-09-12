# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         st = []
#         for i in range(len(tokens)):
#             if tokens[i] == "+":
#                 cu = st.pop() + st.pop()
#                 print(cu)
#                 st.append(cu)
#             elif  tokens[i] == "-":
#                 n1 = st.pop()
#                 n2 = st.pop()
#                 cu = n2 - n1
#                 print(cu)
#                 st.append(cu)
#             elif  tokens[i] == "/":
#                 n1 = st.pop()
#                 n2 = st.pop()
#                 cu = n2 // n1
#                 print(cu)
#                 st.append(cu)
#             elif  tokens[i] == "*":
#                 n1 = st.pop()
#                 n2 = st.pop()
#                 cu = n2 * n1
#                 print(cu)
#                 st.append(cu)
#             else:
#                 num = int(tokens[i])
#                 st.append(num)
#         return st[-1]








class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                st.append(st.pop() + st.pop())
            elif tokens[i] == "-":
                n1 = st.pop()
                n2 = st.pop()
                st.append(n2 - n1)  # Correct order for subtraction
            elif tokens[i] == "/":
                n1 = st.pop()
                n2 = st.pop()
                # Ensure truncation towards zero instead of floor division
                st.append(int(n2 / n1))  
            elif tokens[i] == "*":
                st.append(st.pop() * st.pop())
            else:
                st.append(int(tokens[i]))
        return st[-1]
