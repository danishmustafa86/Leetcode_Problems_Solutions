class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adjs = defaultdict(list)
        for pre, crs in prerequisites:
            adjs[crs].append(pre)
        
        def dfs(crs):
            if crs not in preMap:
                preMap[crs] = set()
                for preval in adjs[crs]:
                    preMap[crs] |= dfs(preval)
                preMap[crs].add(crs)
            return preMap[crs]

        preMap = {}
        for course in range(numCourses):
            dfs(course)
        
        ans = []
        for pre, crs in queries:
            ans.append( pre in preMap[crs])

        return ans
        