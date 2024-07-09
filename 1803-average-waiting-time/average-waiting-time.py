class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cur_time = 0
        total_time = 0
        for arrival, duration in customers:
            if cur_time < arrival:
                cur_time = arrival
            cur_time += duration
            total_time += cur_time - arrival

        return total_time / len(customers)