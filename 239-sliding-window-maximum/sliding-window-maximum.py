from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Initialize a deque to store indices of elements in the current window
        deque_index = deque()
        # List to store the maximums for each sliding window
        maxans = []

        # Loop over all elements in nums
        for i in range(len(nums)):
            # Remove the element from the front of the deque if it's out of the current window
            # The window is [i-k+1, i], so if deque_index[0] == i-k, it's outside the window
            if deque_index and deque_index[0] == i - k:
                deque_index.popleft()

            # Maintain the deque in decreasing order of values
            # If the current element nums[i] is greater than the element at the back of the deque,
            # we remove the element at the back because it can't be the maximum in future windows
            while deque_index and nums[deque_index[-1]] < nums[i]:
                deque_index.pop()

            # Add the current element's index to the deque
            deque_index.append(i)

            # Once we've processed at least the first k elements,
            # the window starts moving forward. We should start recording the maximum.
            # The maximum for the current window is at the front of the deque.
            if i >= k - 1:
                maxans.append(nums[deque_index[0]])

        # Return the list of maximums for each sliding window
        return maxans































# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         maxans = []
#         win = nums[:k]
#         maxans.append(max(win))
#         for i in range(k,len(nums)):
#             win.pop(0)
#             win.append(nums[i])
#             maxans.append(max(win))
#         return maxans 