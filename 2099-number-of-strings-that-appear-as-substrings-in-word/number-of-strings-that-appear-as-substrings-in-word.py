# class Solution:
#     def numOfStrings(self, patterns: List[str], word: str) -> int:
#         num1: int = 0;
#         for (j = 0; j < patterns.length; j++)
#             if word.includes(patterns[j]): 
#                 num1++
        

    
#         return num1;
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        num1 = 0
        for pattern in patterns:
            if pattern in word:
                num1 += 1
        return num1