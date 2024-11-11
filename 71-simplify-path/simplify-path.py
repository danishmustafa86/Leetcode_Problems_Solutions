class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        for s in path + "/" :
            if s == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != "." and cur != "":
                    stack.append(cur)
                cur = ""
            else:
                cur += s

        return "/" + "/".join(stack)
            


#  /../abc//./dfc/       