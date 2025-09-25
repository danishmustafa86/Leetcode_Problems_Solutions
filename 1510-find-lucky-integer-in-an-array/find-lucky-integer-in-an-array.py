class Solution:
    def findLucky(self, arr: List[int]) -> int:
        array=[-1]
        nums=set(arr)
        for i in nums:
            if arr.count(i) == i:
                array.append(i)
        return max(array)