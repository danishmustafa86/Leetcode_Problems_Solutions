class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hsh = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        n = 0
        l = len(digits)
        if l == 0 :
            return []
        if l == 1 :
            n = int(digits)
            return list(hsh[n])
        old = [""] 
        for i in digits:
            new = []

            # n = int(digits[i])
            # cur = list(hsh[n])
            for j in old:
                for k in hsh[int(i)]:
                    new.append(j + k)
            old = new
                



        return new