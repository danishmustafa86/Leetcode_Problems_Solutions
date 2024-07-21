
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def topological_sort(conditions):
            graph = defaultdict(list)
            indegree = {i: 0 for i in range(1, k + 1)}
            
            for u, v in conditions:
                graph[u].append(v)
                indegree[v] += 1
            
            queue = deque([node for node in range(1, k + 1) if indegree[node] == 0])
            topo_order = []
            
            while queue:
                node = queue.popleft()
                topo_order.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            
            if len(topo_order) == k:
                return topo_order
            else:
                return []
        
        row_order = topological_sort(rowConditions)
        col_order = topological_sort(colConditions)
        
        if not row_order or not col_order:
            return []
        
        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}
        
        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num
        
        return matrix