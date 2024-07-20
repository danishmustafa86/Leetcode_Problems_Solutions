class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows, cols = len(rowSum), len(colSum)
        matrix = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                # Set the value to be the minimum of the current row sum and column sum
                value = min(rowSum[i], colSum[j])
                matrix[i][j] = value
                # Subtract the value from the row sum and column sum
                rowSum[i] -= value
                colSum[j] -= value
        
        return matrix