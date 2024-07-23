class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums.reverse()
        arr = []
        x = {}
        for val in nums:
            if val in x:
                x[val] += 1
            else:
                x[val] = 1
        new_dict = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
        for val in new_dict:
            while new_dict[val] > 0:
                arr.append(val)
                new_dict[val] -= 1
        return arr
