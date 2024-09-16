class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = []
        mini = float("inf")

        for time in timePoints:
            hours, minutes = map(int,time.split(":"))
            arr.append(hours*60 + minutes)

        arr.sort()
        for  i in range(1,len(arr)):
            cur = arr[i] - arr[i-1]
            mini = min(mini, cur)
        
        mini = min(mini, 1440 - (arr[-1] - arr[0]))

        return mini