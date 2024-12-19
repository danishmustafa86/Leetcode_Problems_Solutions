class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Initialize variables
        max_seen = 0
        chunks = 0

        # Iterate through the array
        for i, num in enumerate(arr):
            # Update the maximum value seen so far
            max_seen = max(max_seen, num)

            # If the maximum value seen so far equals the current index,
            # it means we can form a chunk up to this point.
            if max_seen == i:
                chunks += 1

        return chunks