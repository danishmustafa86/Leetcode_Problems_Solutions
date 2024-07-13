from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # Create a list of tuples with (position, health, direction, original_index)
        robots = [(positions[i], healths[i], directions[i], i) for i in range(len(positions))]
        
        # Sort robots based on their positions
        robots.sort()
        
        stack = []
        
        for pos, health, direction, index in robots:
            if direction == 'R':
                stack.append((pos, health, direction, index))
            else:
                while stack and stack[-1][2] == 'R' and stack[-1][1] < health:
                    _, r_health, _, _ = stack.pop()
                    health -= 1
                if stack and stack[-1][2] == 'R':
                    if stack[-1][1] == health:
                        stack.pop()
                        health = 0
                    else:
                        stack[-1] = (stack[-1][0], stack[-1][1] - 1, stack[-1][2], stack[-1][3])
                        health = 0
                if health > 0:
                    stack.append((pos, health, direction, index))
        
        # Extract the surviving robots and their health in the original order
        surviving_healths = sorted([(idx, health) for _, health, _, idx in stack])
        return [health for idx, health in surviving_healths]

# Example usage
solution = Solution()
positions = [5, 46, 12]
healths = [3, 27, 43]
directions = "RLL"
print(solution.survivedRobotsHealths(positions, healths, directions))  # Expected Output: [27, 42]
