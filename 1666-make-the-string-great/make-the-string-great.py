class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        for val in s:
            if stk and stk[-1] != val and stk[-1].lower() == val.lower():
                stk.pop()
            else:
                stk.append(val)
        return "".join(stk)


