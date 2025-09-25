from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        # Create a list of tuples with (position, health, direction, original_index)
        robots = [(positions[i], healths[i], directions[i], i) for i in range(n)]
        robots.sort()
        i = 0
        while i < len(robots) - 1:
            if robots[i][2] == 'R' and robots[i + 1][2] == 'L':
                if robots[i][1] == robots[i + 1][1]:
                    robots.pop(i)
                    robots.pop(i)  
                    i = max(i - 1, 0) 
                elif robots[i][1] > robots[i + 1][1]:
                    robots[i] = (robots[i][0], robots[i][1] - 1, 'R', robots[i][3])
                    robots.pop(i + 1)
                else:
                    robots[i + 1] = (robots[i + 1][0], robots[i + 1][1] - 1, 'L', robots[i + 1][3])
                    robots.pop(i)
                i = max(i - 1, 0)
            else:
                i += 1
        
        surviving_healths = [0] * n
        for pos, health, _, original_index in robots:
            surviving_healths[original_index] = health
        
        surviving_healths = [health for health in surviving_healths if health > 0]
        
        return surviving_healths

