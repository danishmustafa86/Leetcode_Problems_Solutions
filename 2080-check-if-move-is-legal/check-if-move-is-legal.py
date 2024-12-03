class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        directions = [[1,1],[-1,-1],[1,-1],[-1,1],[1,0],[0,1],[-1,0],[0,-1]]
        Rows, Cols = len(board), len(board[0])
        board[rMove][cMove] = color

        def legal( rMove, cMove, direc, color):
            dr, dc = direc
            rows, cols = dr + rMove, dc + cMove
            level = 1
            while (0 <= rows < Rows) and (0 <= cols < Cols):
                level += 1
                if board[rows][cols] == ".": return False
                if board[rows][cols] == color: 
                    return level >= 3
                rows, cols = rows + dr, cols + dc

        for d in directions:
            if legal( rMove, cMove, d, color):
                return True
        return False