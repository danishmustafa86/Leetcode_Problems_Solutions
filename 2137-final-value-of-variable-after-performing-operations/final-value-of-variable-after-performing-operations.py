class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        plus = ["++X", "X++"]
        minus = ["--X", "X--"]
        for i in range(len(operations)):
            if operations[i] in plus:
                x += 1
            else:
                x -= 1
        return x





        # l ,r = 0, len(operations)
        # while l<r:
        #     if operations[l] in plus:
        #         x += 1
        #     else:
        #         x -= 1
        #     if operations[r] in plus:
        #         x += 1
        #     else:
        #         x -= 1
        #     l += 1
        #     r -= 1