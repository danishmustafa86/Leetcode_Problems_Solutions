class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        # arr  = []
        # def fun(i,res):
        #     if len(res) == k and res not in arr:
        #         arr.append(res[:])
        #         return
        #     if i > n:
        #         return
        #     res.append(i)
        #     fun(i+1, res)
        #     res.pop()
        #     fun(i+1,res)

        # fun(1, [])
        # return arr























        resArr = []
        cur = []
        def dfs(i):
            if i == n + 1:
                resArr.append(cur.copy())
                return
            cur.append(i)
            dfs( i+1 )
            cur.pop()
            dfs( i+1 )
        
        dfs(1)
        ans = []
        for i in resArr:
            if len(i) == k:
                ans.append(i)
        return ans