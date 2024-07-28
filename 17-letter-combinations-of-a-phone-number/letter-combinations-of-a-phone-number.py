# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         hsh = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
#         n = 0
#         l = len(digits)
#         if not digits :
#             return []
#         if l == 1 :
#             n = int(digits)
#             return list(hsh[n])
#         old = [""] 
#         for i in digits:
#             new = []

#             # n = int(digits[i])
#             # cur = list(hsh[n])
#             for j in old:
#                 for k in hsh[int(i)]:
#                     new.append(j + k)
#             old = new
                
#         return new

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hsh = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        n = 0
        l = len(digits)
        if not digits :
            return []
        if l == 1 :
            n = int(digits)
            return list(hsh[n])
        old =  [""]
        for i in range(l - 1,-1,-1):
            new = []

            n = int(digits[i])
            cur = list(hsh[n])
            for j in cur:
                for k in old:
                    new.append(j + k)
            old = new
                
        return new