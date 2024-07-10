class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_list = list(t)
        for val in s:
            if val in t_list:
                t_list.remove(val)
        return "".join(t_list)