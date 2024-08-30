class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        newstr = s * 2
        print(newstr)
        newstr = newstr[1:-1]
        print(newstr)
        if (s in newstr):
            return True
        else:
            return False
        
# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:

#         sublen = 1
#         for i in range(len(s)//2):

#             substr = s[:sublen]
#             substr = substr * (len(s)//sublen)
#             if s == substr:
#                 return True
            
#             sublen += 1

#         return False
        
            