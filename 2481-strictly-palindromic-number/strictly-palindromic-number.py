class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def isPalindrome(bn):
            i = 0
            j = len(bn)-1
            while i<j:
                if bn[i] != bn[j]:
                    return False
                i += 1 
                j -= 1
            return True
        for i in range(2,n-1):
            bn = ""
            nn = n
            while nn:
                bn += str(nn % i)
                nn //= i
            if not isPalindrome(bn):
                return False
        return True