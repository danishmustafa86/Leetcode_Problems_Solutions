class Solution:
    def findLucky(self, arr: List[int]) -> int:
        array=[-1]
        luckySet= set(arr)
        for i in luckySet:
            if arr.count(i) == i:
                array.append(i)
        return max(array) 
                 
