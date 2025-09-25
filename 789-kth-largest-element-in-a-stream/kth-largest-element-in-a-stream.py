class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxHeap, self.k = nums, k
        heapq.heapify(self.maxHeap)
        while len(self.maxHeap) > self.k:
            heapq.heappop(self.maxHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.maxHeap, val)
        if len(self.maxHeap) > self.k:
            heapq.heappop(self.maxHeap)
        return self.maxHeap[0]






























    # def __init__(self, k: int, nums: List[int]):
    #     self.minHeap, self.k = nums, k
    #     heapq.heapify(self.minHeap)
    #     while len(self.minHeap) > self.k:
    #         heapq.heappop(self.minHeap)

    # def add(self, val: int) -> int:
    #     heapq.heappush(self.minHeap, val)
    #     if len(self.minHeap) > self.k:
    #         heapq.heappop(self.minHeap)
    #     return self.minHeap[0]
        
