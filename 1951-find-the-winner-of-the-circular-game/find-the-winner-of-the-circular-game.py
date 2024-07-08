class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = []
        j = 0

        for i in range(1,n+1):
            arr.append(i)

        while len(arr) > 1:
            j += k - 1
            j = j % len(arr)
            arr.remove(arr[j]) 


        winner = arr[0]
        return winner