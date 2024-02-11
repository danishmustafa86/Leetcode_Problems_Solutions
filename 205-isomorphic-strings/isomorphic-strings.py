# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#        stST,tsTS={},{}
#        for c1,c2 in zip(s,t):
#            if (c1 in stST and stST[c1] != c2) or ( c2 in tsTS and tsTS[c2]!=c1) :
#                 return False
#             stST[c1] = c2
#             tsST[c2] = c1
#         return True
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stST, tsTS = {}, {}
        for c1, c2 in zip(s, t):
            if (c1 in stST and stST[c1] != c2) or (c2 in tsTS and tsTS[c2] != c1):
                return False
            stST[c1] = c2
            tsTS[c2] = c1
        return True
