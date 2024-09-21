class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        arr = []

        def dfs(cur):
            if cur > n:
                return 
            arr.append(cur)
            for i in range(0,10):
                inner_cur = cur * 10 + i
                if inner_cur > n:
                    return
                dfs(inner_cur)
        for i in range(1,10):
            dfs(i)

        return arr
    
