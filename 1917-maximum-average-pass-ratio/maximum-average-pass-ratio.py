import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Max-Heap to store the ratio improvements with the extra student
        # We will store the negative of the improvement to simulate a max-heap using heapq (which is a min-heap by default)
        heap = []

        # Calculate the initial ratio and the possible improvements for each class
        for a, b in classes:
            # Calculate the difference in ratio if we add one extra student to the class
            improvement = (a + 1) / (b + 1) - a / b
            # Push (-improvement, a, b) so that heapq can pop the largest improvement
            heapq.heappush(heap, (-improvement, a, b))

        # Distribute the extra students
        for _ in range(extraStudents):
            # Pop the class with the maximum improvement
            improvement, a, b = heapq.heappop(heap)
            # Add one student to the class
            a += 1
            b += 1
            # Recompute the new improvement for this class and push it back to the heap
            new_improvement = (a + 1) / (b + 1) - a / b
            heapq.heappush(heap, (-new_improvement, a, b))

        # Now, compute the final average ratio
        total_ratio = 0
        for improvement, a, b in heap:  # Corrected the unpacking
            total_ratio += a / b

        # Return the final average ratio
        return total_ratio / len(classes)
