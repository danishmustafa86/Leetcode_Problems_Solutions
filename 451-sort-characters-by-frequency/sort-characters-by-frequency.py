# class Solution:
#     def frequencySort(self, s: str) -> str:
#         # s = list(s)
#         # s.sort()
#         # s.reverse()
#         hsh = {}
#         arr = []
#         for i in s:
#             if i in hsh:
#                 hsh[i] += 1
#             else:
#                 hsh[i] = 1
#         shsh = sorted( hsh.items(), key = lambda x: (-x[1],x[0]))
#         for k, v in shsh:
#             arr.append(k*v)
#         return "".join(arr)










class Solution:
    def frequencySort(self, s: str) -> str:
        s = list(s)
        s.sort()
        # s.reverse()
        hsh = {}
        arr = []
        for i in s:
            if i in hsh:
                hsh[i] += 1
            else:
                hsh[i] = 1

        # Correcting the loop and usage of the while loop to append characters
        shsh = {k: hsh[k] for k in sorted(hsh, key = hsh.get, reverse = True)}
        
        for v in shsh:
            count = shsh[v]
            while count > 0:
                arr.append(v)
                count -= 1

        return "".join(arr)

# Example usage
solution = Solution()
print(solution.frequencySort("tree"))  # Output: "eert"
print(solution.frequencySort("cccaaa"))  # Output: "aaaccc" or "cccaaa"
print(solution.frequencySort("Aabb"))  # Output: "bbAa" or "Aabb"
