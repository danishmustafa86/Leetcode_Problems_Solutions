class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        # Initialize counters for rows and columns
        for i in range(n):
            row_counts = [0] * n
            col_counts = [0] * n

            for j in range(n):
                # Check for duplicates in rows
                if row_counts[matrix[i][j] - 1] != 0:
                    return False
                row_counts[matrix[i][j] - 1] += 1

                # Check for duplicates in columns
                if col_counts[matrix[j][i] - 1] != 0:
                    return False
                col_counts[matrix[j][i] - 1] += 1

        return True
