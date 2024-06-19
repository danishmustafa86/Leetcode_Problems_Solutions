class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
    # def minDays(bloomDay, m, k):
        def canMakeBouquets(days):
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                if bouquets >= m:
                    return True
            return False

        if m * k > len(bloomDay):
            return -1

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                right = mid
            else:
                left = mid + 1

        return left if canMakeBouquets(left) else -1

    # Example usage
    # print(minDays([1,10,3,10,2], m=3, k=1))  # Output: 3
    # print(minDays([1,10,3,10,2], m=3, k=2))  # Output: -1
    # print(minDays([7,7,7,7,12,7,7], m=2, k=3))  # Output: 12
