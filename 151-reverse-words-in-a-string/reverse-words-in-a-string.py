class Solution:
    def reverseWords(self, s: str) -> str:
        arr = []
        cur = ""
        for i in range(len(s)):
            if s[i] == " ":
                if len(cur) != 0:
                    arr.append(cur)
                cur = ""
            else:
                cur += s[i]
        if len(cur) != 0:
            arr.append(cur)
        arr.reverse()
        res = ""
        for i in range(len(arr)):
            if i != len(arr) - 1:
                res += arr[i] + " "
            else:
                res += arr[i]
        print(arr)
        print(res)
        return res