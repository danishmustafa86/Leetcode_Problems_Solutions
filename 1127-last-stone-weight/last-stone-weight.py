# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:



        # stones = [-s for s in stones]
        # heapq.heapify(stones)
        # while len(stones) > 1:
        #     first = heapq.heappop(stones)
        #     second = heapq.heappop(stones)
        #     if second > first:
        #         heapq.heappush(stones, first - second)
        # stones.append(0)
        # return abs(stones[0])








class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                v1  = stones.pop()
                v2  = stones.pop()
                stones.append(v1 - v2)
                stones.sort()
        stones.append(0)
        return stones[0] 

