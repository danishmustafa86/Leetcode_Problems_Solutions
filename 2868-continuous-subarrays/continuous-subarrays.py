from collections import deque

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        start = 0
        min_deque = deque()  # Tracks minimum values in the current window
        max_deque = deque()  # Tracks maximum values in the current window
        result = 0

        for end in range(len(nums)):
            # Add current element to deques
            while min_deque and nums[end] < min_deque[-1]:
                min_deque.pop()
            while max_deque and nums[end] > max_deque[-1]:
                max_deque.pop()
            
            min_deque.append(nums[end])
            max_deque.append(nums[end])

            # Shrink window if condition is violated
            while max_deque[0] - min_deque[0] > 2:
                if nums[start] == min_deque[0]:
                    min_deque.popleft()
                if nums[start] == max_deque[0]:
                    max_deque.popleft()
                start += 1

            # Count all subarrays ending at `end`
            result += (end - start + 1)

        return result
