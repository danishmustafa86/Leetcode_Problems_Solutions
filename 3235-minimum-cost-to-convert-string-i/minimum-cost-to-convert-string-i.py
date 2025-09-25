from typing import List, Optional
import sys

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        max_cost = sys.maxsize
        
        # Initialize the cost dictionary with tuples
        cost_dict = {chr(i): {chr(j): max_cost for j in range(ord('a'), ord('z') + 1)} for i in range(ord('a'), ord('z') + 1)}
        
        # Cost to change a character to itself is 0
        for i in range(ord('a'), ord('z') + 1):
            cost_dict[chr(i)][chr(i)] = 0
        
        # Populate the cost dictionary with given transformations
        for o, c, z in zip(original, changed, cost):
            cost_dict[o][c] = min(cost_dict[o][c], z)
        
        # Floyd-Warshall algorithm to find the shortest path
        for k in range(ord('a'), ord('z') + 1):
            for i in range(ord('a'), ord('z') + 1):
                for j in range(ord('a'), ord('z') + 1):
                    if cost_dict[chr(i)][chr(k)] < max_cost and cost_dict[chr(k)][chr(j)] < max_cost:
                        cost_dict[chr(i)][chr(j)] = min(cost_dict[chr(i)][chr(j)], cost_dict[chr(i)][chr(k)] + cost_dict[chr(k)][chr(j)])
        
        # Calculate the total cost
        total_cost = 0
        for s_char, t_char in zip(source, target):
            if cost_dict[s_char][t_char] == max_cost:
                return -1
            total_cost += cost_dict[s_char][t_char]
        
        return total_cost

# Example usage
solution = Solution()
source = "abcd"
target = "acbe"
original = ["a", "b", "c", "c", "e", "d"]
changed = ["b", "c", "b", "e", "b", "e"]
cost = [2, 5, 5, 1, 2, 20]
print(solution.minimumCost(source, target, original, changed, cost))  # Output: 28

source = "aaaa"
target = "bbbb"
original = ["a", "c"]
changed = ["c", "b"]
cost = [1, 2]
print(solution.minimumCost(source, target, original, changed, cost))  # Output: 12

source = "abcd"
target = "abce"
original = ["a"]
changed = ["e"]
cost = [10000]
print(solution.minimumCost(source, target, original, changed, cost))  # Output: -1
