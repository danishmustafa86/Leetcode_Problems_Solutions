class Solution:
    def findLucky(self, arr: List[int]) -> int:
        array=[-1]
        lucky=0
        Max=0
        luckySet= set(arr)
        for i in luckySet:
            if arr.count(i) == i:
                array.append(arr.count(i))
        return max(array) 
                 
