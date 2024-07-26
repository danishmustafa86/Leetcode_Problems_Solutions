class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return (set(nums1)) & (set(nums2))
        hash_map = {}
        arr = []
        for i in nums1:
            hash_map[i] = i
        for i in nums2:
            if i in hash_map:
                arr.append(i)
                del hash_map[i]
        return arr