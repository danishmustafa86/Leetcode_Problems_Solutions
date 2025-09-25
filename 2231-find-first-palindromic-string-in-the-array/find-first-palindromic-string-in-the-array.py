class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            lst = list(i)
            lst.reverse()
            lst = "".join(lst)
            if lst == i:
                return i
        return ""