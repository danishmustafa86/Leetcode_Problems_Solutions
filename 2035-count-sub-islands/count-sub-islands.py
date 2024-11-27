class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        Rows, Cols  = len(grid1), len(grid1[0])
        visit = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r== Rows or c == Cols or (r,c) in visit or grid2[r][c] == 0:
                return True

            visit.add((r,c))
            result = True
            if grid1[r][c] == 0:
                result = False

            result = dfs(r-1,c) and result
            result = dfs(r+1,c) and result
            result = dfs(r,c - 1) and result
            result = dfs(r,c + 1) and result

            return result

        count = 0
        for r in range(Rows):
            for c in range(Cols):
                if (r,c) not in visit and dfs(r,c) and grid2[r][c]:
                    count += 1
        
        return count