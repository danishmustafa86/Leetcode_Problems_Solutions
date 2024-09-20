class Solution:
    def shortestPalindrome(self, s: str) -> str:

        for i in range(len(s), 0,-1):
            front = s[:i]
            rev = front[::-1]
            cur = s[i:]
            if front == rev:
                return cur[::-1] + s
        return ""

































        rev = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(rev[i:]):
                return rev[:i] + s









        # for i in range(len(s), 0, -1):
        #     back = s[:i]
        #     rev = back[::-1]
        #     front = s[i:]
        #     if  back == rev:
        #         return front[::-1] + s
        # return ""