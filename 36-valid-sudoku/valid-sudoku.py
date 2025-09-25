class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows and columns
        for i in range(9):
            row, col = [], []
            for j in range(9):
                if board[i][j] != ".":  # Check row uniqueness
                    row.append(board[i][j])
                if board[j][i] != ".":  # Check column uniqueness
                    col.append(board[j][i])
            # If any row or column has duplicates, return False
            if len(row) != len(set(row)) or len(col) != len(set(col)):
                return False

        # Function to check if a 3x3 sub-box is valid
        def isValidBox(start_row, start_col):
            seen = set()
            for i in range(3):
                for j in range(3):
                    value = board[start_row + i][start_col + j]
                    if value != ".":  # Only check filled cells
                        if value in seen:
                            return False
                        seen.add(value)
            return True  # Return True if no duplicates

        # Check all 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not isValidBox(i, j):
                    return False

        return True  # If everything is valid, return True
