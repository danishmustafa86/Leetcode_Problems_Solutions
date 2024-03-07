# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         arr=[]
#         for i in range(len(numbers)):
#             for j in range(i+1,len(numbers)):
#                 if numbers[i]+numbers[j]==target:
#                     arr.append([i+1,j+1])
#         return arr

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         arr = []
#         for i in range(len(numbers)):
#             for j in range(i+1, len(numbers)):
#                 if numbers[i] + numbers[j] == target:
#                     arr.append([i+1, j+1])
#         if not arr:
#             return []  # Return an empty list if no pair is found
#         return arr


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_indices = {}
        
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement] + 1, i + 1]
            num_indices[num] = i
        
        return []  # Return empty list if no pair is found
