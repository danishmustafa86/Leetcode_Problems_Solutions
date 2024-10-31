class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        area = 0
        visit, arr = set(), []
        Rows, Cols = len(grid), len(grid[0])

        def dfs( r, c):
            visit.add((r,c))
            q = deque()
            q.append((r,c))
            cur = 1
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    new_r, new_c  = dr + row, dc + col
                    if new_r in range(Rows) and new_c in range(Cols) and (new_r, new_c) not in visit and grid[new_r][new_c] == 1:
                        visit.add((new_r, new_c))
                        cur += 1
                        q.append((new_r, new_c))
            arr.append(cur)

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    dfs(r, c)
        return max(arr) if arr else 0