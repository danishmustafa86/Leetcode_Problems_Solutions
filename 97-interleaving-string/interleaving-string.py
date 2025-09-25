class Solution:

    m = 0
    n = 0
    N = 0
    memo = {}
    
    def sol(self , i , j , s1 , s2 , s3) -> bool:
        if (i, j) in self.memo:
            return self.memo[(i,j)]

        # when we will find all the possible soltuions 
        if i == self.m and j==self.n and i+j==self.N:
            return True

        # if the characters are only found 
        if i+j >= self.N:
            return False

        flag = False

        if i < self.m and s3[i+j] == s1[i]:
            flag = self.sol(i+1, j, s1,s2,s3)
        if flag:
            self.memo[(i,j)] = flag
            return flag

        if j< self.n  and s3[i+j]== s2[j]:
            flag = self.sol(i, j+1, s1,s2,s3)

        self.memo[(i,j)] = flag
        return flag

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.m = len(s1)
        self.n = len(s2)
        self.N = len(s3)

        if self.m + self.n != self.N:
            return False
        
        self.memo = {}

        return self.sol(0 ,0 , s1, s2 , s3)