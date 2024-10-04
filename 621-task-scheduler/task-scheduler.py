class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-ctn for ctn in  count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()
        while q or maxHeap:
            time += 1
            if maxHeap:
                ctn = 1 + heapq.heappop(maxHeap)
                if ctn:
                    q.append([ctn,time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
