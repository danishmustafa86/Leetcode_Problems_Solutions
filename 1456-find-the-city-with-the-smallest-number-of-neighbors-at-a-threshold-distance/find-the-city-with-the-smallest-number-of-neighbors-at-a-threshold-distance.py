class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize the distance matrix
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Distance to itself is zero
        for i in range(n):
            dist[i][i] = 0
        
        # Fill initial distances based on the edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Floyd-Warshall algorithm to compute shortest paths between all pairs of cities
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Find the city with the smallest number of reachable cities within the distance threshold
        min_count = float('inf')
        best_city = -1
        
        for i in range(n):
            count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            
            # Update the result if a city with fewer or the same count but a greater index is found
            if count < min_count or (count == min_count and i > best_city):
                min_count = count
                best_city = i
        
        return best_city
