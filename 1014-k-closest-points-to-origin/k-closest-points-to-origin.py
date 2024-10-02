class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for i in range(len(points)):
            cur = abs(points[i][0])**2 + abs(points[i][1])**2
            arr.append((   points[i], cur  ))

        arr = sorted(arr, key=lambda x:x[1])
        ans = []
        for i in range(0,k):
            ans.append(arr[i][0])
        return ans