class Solution:
        def findRelativeRanks(self, score: List[int]) -> List[str]:
            # Sort the scores in descending order while keeping track of the original indices
            sorted_scores = sorted(enumerate(score), key=lambda x: -x[1])
            
            # Create an array to store the results
            result = [""] * len(score)
            
            # Assign the ranks based on the sorted order
            for rank, (idx, score) in enumerate(sorted_scores):
                if rank == 0:
                    result[idx] = "Gold Medal"
                elif rank == 1:
                    result[idx] = "Silver Medal"
                elif rank == 2:
                    result[idx] = "Bronze Medal"
                else:
                    result[idx] = str(rank + 1)
            
            return result
