class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # stack1 = []
        # for i in s:
        #     if  i != "#":
        #         stack1.append(i)
        #     elif stack1:
        #         stack1.pop()
        
        # stack2 = []
        # for i in t:
        #     if  i != "#":
        #         stack2.append(i)
        #     elif stack2:
        #         stack2.pop()
        # return "".join(stack1) == "".join(stack2)

        st1, st2 = [],[]
        for i in s:
            if i != "#":
                st1.append(i)
            elif st1:
                st1.pop()
        for i in t:
            if i != "#":
                st2.append(i)
            elif st2:
                st2.pop()
        return "".join(st1) == "".join(st2)