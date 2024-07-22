
class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        # Append the new request time
        self.queue.append(t)
        # Calculate the start of the range
        start = t - 3000
        # Remove requests that are older than the 3000 ms range
        while self.queue and self.queue[0] < start:
            self.queue.popleft()
        # The length of the queue gives the number of recent requests
        return len(self.queue)
