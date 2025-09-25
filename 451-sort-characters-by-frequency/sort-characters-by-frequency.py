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
        hsh = {}
        arr = []
        for i in s:
            if i in hsh:
                hsh[i] += 1
            else:
                hsh[i] = 1

        # Sorting the dictionary based on frequency in descending order
        shsh = {k: hsh[k] for k in sorted(hsh, key=hsh.get, reverse=True)}
        
        for k, v in shsh.items():
            arr.append(k * v)

        return "".join(arr)
