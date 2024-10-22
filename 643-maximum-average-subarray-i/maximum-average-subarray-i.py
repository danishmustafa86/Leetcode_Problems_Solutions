class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # # Initial sum of the first `k` elements
        # current_sum = sum(nums[:k])
        # max_sum = current_sum

        # # Slide the window over the array
        # for i in range(k, len(nums)):
        #     current_sum += nums[i] - nums[i - k]
        #     max_sum = max(max_sum, current_sum)

        # return max_sum / k
        cur_sum = sum(nums[:k])
        max_sum = cur_sum
        for i in range(k, len(nums)):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]
            max_sum = max( cur_sum, max_sum)

        return max_sum / k
