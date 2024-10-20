class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = deque()
        for c in expression:
            if c == "(" or c == ",":
                continue
            if c in ["!", "&", "|", "f", "t"]:
                st.append(c)
            if c == ")":
                has_True = False
                has_False = False
                while st[-1] not in ["!", "&", "|"]:
                    cur = st.pop()
                    if cur == "f":
                        has_False = True
                    elif cur == "t":
                        has_True = True
                op = st.pop()
                if op == "!":
                    st.append("t" if not has_True else "f")
                elif op == "&":
                    st.append("f" if has_False else "t")
                else:
                    st.append("t" if has_True else "f")
        return st[-1] == "t"
                