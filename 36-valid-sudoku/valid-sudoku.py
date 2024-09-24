class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row, col = [], []
            for j in range(9):
                if board[i][j] != ".":
                    row.append(board[i][j])
                if board[j][i] != ".":
                    col.append(board[j][i])
            if len(row) != len(set(row)) or len(col) != len(set(col)):
                return False

        # function for checking box uniqueness
        
        def isValid(ielm, jelm):
            seen = set()
            for i in range(3):
                for j in range(3):
                    value = board[i + ielm][ j + jelm]
                    if value != ".":
                        if value in seen:
                            return False
                        seen.add(board[i + ielm][ j + jelm])
            return True

        for i in range(0, 9, 3):
            for j in range(0,9,3):
                if not isValid(i,j):
                    return False
        return True
