from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums)
        indexed_nums = list(enumerate(nums))  # (original_index, value)

        def count(arr, low, mid, high):
            temp = []
            right_counter = 0
            left = low
            right = mid + 1

            while left <= mid and right <= high:
                if arr[left][1] <= arr[right][1]:
                    counts[arr[left][0]] += right_counter
                    temp.append(arr[left])
                    left += 1
                else:
                    right_counter += 1
                    temp.append(arr[right])
                    right += 1

            while left <= mid:
                counts[arr[left][0]] += right_counter
                temp.append(arr[left])
                left += 1

            while right <= high:
                temp.append(arr[right])
                right += 1

            for i in range(low, high + 1):
                arr[i] = temp[i - low]

        def ms(arr, low, high):
            if low >= high:
                return
            mid = (low + high) // 2
            ms(arr, low, mid)
            ms(arr, mid + 1, high)
            count(arr, low, mid, high)

        ms(indexed_nums, 0, len(nums) - 1)
        return counts
