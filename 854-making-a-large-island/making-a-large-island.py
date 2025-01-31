from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def exploreIsland(grid, isIsland, row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 1:
                return 0
            grid[row][col] = isIsland
            return 1 + exploreIsland(grid, isIsland, row, col + 1) + exploreIsland(grid, isIsland, row, col - 1) + exploreIsland(grid, isIsland, row + 1, col) + exploreIsland(grid, isIsland, row - 1, col)
        
        hsh = {}
        isIsland = 2
        
        # Step 1: Assign unique IDs to islands and store their sizes
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    hsh[isIsland] = exploreIsland(grid, isIsland, row, col)
                    isIsland += 1

        # Step 2: If grid is fully filled with 1s, return its size
        if len(hsh) == 1:
            isIsland -= 1
            if hsh[isIsland] == len(grid) * len(grid[0]):  # Fix multiplication here
                return hsh[isIsland]
            else:
                return hsh[isIsland] + 1  # Adding 1 for a potential conversion

        maxIsland = 1

        # Step 3: Check each 0 cell to see the max island size if flipped to 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    currentIsland = 1
                    Set = set()
                    
                    # Check all four directions
                    if row + 1 < len(grid) and grid[row + 1][col] > 1:
                        Set.add(grid[row + 1][col])
                    if row - 1 >= 0 and grid[row - 1][col] > 1:
                        Set.add(grid[row - 1][col])
                    if col + 1 < len(grid[0]) and grid[row][col + 1] > 1:
                        Set.add(grid[row][col + 1])
                    if col - 1 >= 0 and grid[row][col - 1] > 1:
                        Set.add(grid[row][col - 1])

                    # Fix: Add actual island sizes, not their IDs
                    currentIsland += sum(hsh[i] for i in Set)
                    maxIsland = max(currentIsland, maxIsland)
        
        return maxIsland
