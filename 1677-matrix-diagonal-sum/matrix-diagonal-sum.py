class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        r=len(mat)-1
        for i in range(len(mat)):
            sum += mat[i][i]
            sum += mat[i][r]
            r -=1
        if len(mat)%2 == 1:
            sum -= mat[len(mat)//2][len(mat)//2]
        return sum
