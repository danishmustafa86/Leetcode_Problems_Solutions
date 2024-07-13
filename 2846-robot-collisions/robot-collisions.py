from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        
        # Create a list of tuples with (position, health, direction, original_index)
        robots = [(positions[i], healths[i], directions[i], i) for i in range(n)]
        
        # Sort robots based on their positions
        robots.sort()
        
        i = 0
        while i < len(robots) - 1:
            if robots[i][2] == 'R' and robots[i + 1][2] == 'L':
                if robots[i][1] == robots[i + 1][1]:
                    # Both robots have the same health, remove both
                    robots.pop(i)
                    robots.pop(i)  # After popping i once, the next robot shifts left
                    i = max(i - 1, 0)  # Adjust index after removal
                elif robots[i][1] > robots[i + 1][1]:
                    # Robot i survives, robot i+1 loses 1 health
                    robots[i] = (robots[i][0], robots[i][1] - 1, 'R', robots[i][3])
                    robots.pop(i + 1)
                else:
                    # Robot i+1 survives, robot i loses 1 health
                    robots[i + 1] = (robots[i + 1][0], robots[i + 1][1] - 1, 'L', robots[i + 1][3])
                    robots.pop(i)
                # Reset i to check the previous pair again
                i = max(i - 1, 0)
            else:
                i += 1
        
        # Extract the surviving healths in the original order
        surviving_healths = [0] * n
        for pos, health, _, original_index in robots:
            surviving_healths[original_index] = health
        
        # Remove zeros (robots that did not survive)
        surviving_healths = [health for health in surviving_healths if health > 0]
        
        return surviving_healths

# Example usage
solution = Solution()
positions = [5, 46, 12]
healths = [3, 27, 43]
directions = "RLL"
print(solution.survivedRobotsHealths(positions, healths, directions))  # Expected Output: [27, 42]
