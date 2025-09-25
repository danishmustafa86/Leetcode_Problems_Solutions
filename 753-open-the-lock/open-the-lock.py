from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def get_neighbors(lock: str) -> List[str]:
            neighbors = []
            for i in range(4):
                digit = int(lock[i])
                # Generate the next and previous digit in the lock
                for delta in (-1, 1):
                    new_digit = (digit + delta) % 10
                    neighbors.append(lock[:i] + str(new_digit) + lock[i+1:])
            return neighbors

        # Initialize BFS
        visit = set(deadends)
        q = deque([("0000", 0)])  # (current lock state, turns)
        
        while q:
            lock, turns = q.popleft()
            
            if lock == target:
                return turns
            
            if lock in visit:
                continue
            
            visit.add(lock)
            
            for neighbor in get_neighbors(lock):
                if neighbor not in visit:
                    q.append((neighbor, turns + 1))
        
        return -1
