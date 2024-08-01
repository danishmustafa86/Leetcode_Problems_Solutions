class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums.reverse()
        hsh = {}
        for val in nums:
            if val in hsh:
                hsh[val] += 1
            else:
                hsh[val] = 1
        sorted_hsh = {k:v for k,v in sorted(hsh.items() , key = lambda item:item[1])}
        ans = []
        for val in sorted_hsh:
            while hsh[val] > 0:
                ans.append(val)
                hsh[val] -= 1
        return ans


















        # nums.sort()
        # nums.reverse()
        # x = {}
        # for val in nums:
        #     if val in x:
        #         x[val] += 1
        #     else:
        #         x[val] = 1
        # new_dict = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
        # arr = []
        # for val in new_dict:
        #     while new_dict[val] > 0:
        #         arr.append(val)
        #         new_dict[val] -= 1
        # return arr
