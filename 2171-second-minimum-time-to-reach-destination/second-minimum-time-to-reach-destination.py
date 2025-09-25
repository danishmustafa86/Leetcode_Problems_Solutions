
class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        # Initialize the graph as an adjacency list
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Priority queue to store (current_time, current_node, visit_count)
        pq = [(0, 1, 0)]  # Start with node 1, at time 0, with 0 visits
        
        # Dictionary to store the two shortest times to reach each node
        times = {i: [sys.maxsize, sys.maxsize] for i in range(1, n + 1)}
        times[1][0] = 0  # Start from node 1 with time 0

        while pq:
            current_time, node, visit_count = heappop(pq)

            for neighbor in graph[node]:
                next_time = current_time + time
                # Calculate the waiting time due to traffic lights
                if (current_time // change) % 2 == 1:  # Currently red light
                    next_time += change - (current_time % change)

                # Update the times for the neighbor
                if next_time < times[neighbor][0]:
                    times[neighbor][1] = times[neighbor][0]
                    times[neighbor][0] = next_time
                    heappush(pq, (next_time, neighbor, visit_count + 1))
                elif times[neighbor][0] < next_time < times[neighbor][1]:
                    times[neighbor][1] = next_time
                    heappush(pq, (next_time, neighbor, visit_count + 1))

        # The second minimum time to reach node n
        return times[n][1]
