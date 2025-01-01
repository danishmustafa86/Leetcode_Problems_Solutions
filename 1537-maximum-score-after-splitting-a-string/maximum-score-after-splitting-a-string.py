class Solution:
    def maxScore(self, s: str) -> int:
        maxans = 0
        zeros = 0
        total_zeros = s.count("0")
        ones = s.count("1")
        for i in range(1,len(s)):
            if s[i - 1] == "0":
                zeros += 1
                total_zeros -= 1
            maxans = max( maxans, zeros + (len(s) - total_zeros - i))
        return maxans



# class Solution:
#     def maxScore(self, s: str) -> int:
#         maxans = 0
#         for i in range(len(s)+1):
#             print("first half is ", len(s[0:i]) , "second half is ", len(s[i:]))
#             if s[0:i].count("0") + s[i:].count("1") > maxans:
#                 maxans = s[0:i].count("0") + s[i:].count("1")
#         return maxans
