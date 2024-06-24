class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flip = 0
        q = deque()
        n = len(nums)
        for i in range(n):
            if q and q[0]<i:
                q.popleft()
            if len(q)%2==nums[i]:
                if i+k-1>=n:
                    return -1
                q.append(i+k-1)
                flip+=1
        return flip