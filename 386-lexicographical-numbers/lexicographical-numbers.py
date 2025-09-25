
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # Initialize an empty list to store the result
        arr = []

        # Define a helper function for depth-first search (DFS)
        def dfs(cur):
            # If the current number exceeds n, return to stop further processing
            if cur > n:
                return 
            
            # Append the current number to the result list
            arr.append(cur)
            
            # Explore the next possible numbers by adding digits from 0 to 9
            for i in range(0, 10):  # Change to range(0, 10) to include 0
                inner_cur = cur * 10 + i  # Form the next number by appending digit i
                
                # If the next number exceeds n, stop exploring further
                if inner_cur > n:
                    return
                
                # Recursively call dfs for the next number
                dfs(inner_cur)

        # Start the DFS from each digit from 1 to 9
        for i in range(1, 10):
            dfs(i)

        # Return the result list containing numbers in lexicographical order
        return arr
