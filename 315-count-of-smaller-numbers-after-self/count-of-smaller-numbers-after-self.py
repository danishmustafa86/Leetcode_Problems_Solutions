from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        pairs = list(enumerate(nums))  # (index, value)
        
        def merge_sort(start, end):
            if end - start <= 1:
                return pairs[start:end]
            
            mid = (start + end) // 2
            left = merge_sort(start, mid)
            right = merge_sort(mid, end)
            merged = []
            i = j = 0
            right_count = 0
            
            while i < len(left) and j < len(right):
                if left[i][1] > right[j][1]:
                    # right[j] is smaller, so it's a smaller number to the right of left[i]
                    merged.append(right[j])
                    right_count += 1
                    j += 1
                else:
                    counts[left[i][0]] += right_count
                    merged.append(left[i])
                    i += 1
                    
            # Remaining left items
            while i < len(left):
                counts[left[i][0]] += right_count
                merged.append(left[i])
                i += 1
            # Remaining right items
            while j < len(right):
                merged.append(right[j])
                j += 1

            pairs[start:end] = merged
            return merged
        
        merge_sort(0, n)
        return counts
