class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        res = [0] * n  # Initialize the result list with 0s
        stack = []  # Stack to keep indices of temp

        for i in range(n):
            # Check if the current temp is higher than the temp at the index of the stack's top
            while stack and temp[i] > temp[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)  # Push current index to stack

        return res

        
