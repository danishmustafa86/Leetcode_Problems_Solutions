class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        visit = set()
        changes = 0
        neighbours = { city:[] for city in range(n)}
        edges = { (a,b) for a,b in connections}

        for a,b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)
        def dfs(city):
            nonlocal changes, visit, neighbours, edges
            for neighbour in neighbours[city]:
                if neighbour in visit:
                    continue
                if (neighbour, city) not in edges:
                    changes += 1
                visit.add(neighbour)
                dfs(neighbour)


        visit.add(0)
        dfs(0)
        return changes