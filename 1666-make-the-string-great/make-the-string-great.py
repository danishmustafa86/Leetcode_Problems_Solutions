class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        for val in s:
            if stk and stk[-1] != val and stk[-1].lower() == val.lower():
                stk.pop()
            else:
                stk.append(val)
        return "".join(stk)













        # stk = []
        # for val in s:
        #     if stk and stk[-1] != val and val.lower() == stk[-1].lower():
        #         stk.pop()
        #     else:
        #         stk.append(val)
        # return "".join(stk)
