class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        arr = []
        time,wait = customers[0][0], customers[0][0]
        for i in range(len(customers)):
            time += customers[i][1]
            print(time)
            wait = time - customers[i][0]
            arr.append(wait)

            if customers[i][0]  > time - customers[i][1]:
                time = customers[i][0] + customers[i][1]
                wait = time - customers[i][0]
                arr.pop()
                arr.append(wait)
        print(arr,sum(arr))
        return sum(arr) / len(customers)