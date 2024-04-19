# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         i, j, max_len=0, 0, 0
#         my_set = set()
#         while j < len(s):
#             if s[j] not in my_set:
#                 my_set.add(s[j])
#                 j += 1
#                 max_len = max(max_len, len(my_set))
#                 print("my_set is", my_set)
#             else:
#                 my_set.remove(s[i])
#                 print("my_set is", my_set)
#                 i += 1
#         return max_len

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, max_len = 0, 0, 0
        my_set = set()
        while j < len(s):
            if s[j] not in my_set:
                my_set.add(s[j])
                j += 1
                max_len = max(max_len, len(my_set))
                # print("my_set is", my_set)
            else:
                my_set.remove(s[i])
                i += 1
        return max_len

