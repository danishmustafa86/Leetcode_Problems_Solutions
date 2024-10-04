class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # heap = []
        # for val in points:
        #     cur = val[0]**2 + val[1]**2
        #     heapq.heappush(heap, (cur, val))
        # result = [heapq.heappop(heap)[1] for _ in range(k)]
        # return result

        heap = []
        for val in points:
            cur = val[0]**2 + val[1]**2
            heapq.heappush(heap, (cur,val))
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result