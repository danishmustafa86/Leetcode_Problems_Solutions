from typing import List
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        maxHeap = [-val for val in gifts]
        heapq.heapify(maxHeap)

        while k > 0 and maxHeap:
            maxElm = -heapq.heappop(maxHeap)
            reduced = int(math.sqrt(maxElm))
            heapq.heappush(maxHeap, -reduced)
            k -= 1
        return -sum(maxHeap)