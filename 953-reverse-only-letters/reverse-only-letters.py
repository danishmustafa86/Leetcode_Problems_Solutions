class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s= list(s)
        l,r = 0, len(s)-1
        while l<r:
            if s[l].isalpha() and s[r].isalpha():
                s[l],s[r] = s[r],s[l]
                r -= 1
                l += 1
            elif not  s[r].isalpha():
                r -= 1
            else:
                l += 1
        return "".join(s)