class Solution:
    def is_integer(self, s):  # Add self as the first parameter
        try:
            int(s)
            return True
        except ValueError:
            return False

    def clearDigits(self, s: str) -> str:
        arr = []
        for i in range(len(s)):
            if self.is_integer(s[i]):  # Use self to call the is_integer method
                if arr:
                    arr.pop()
            else:
                arr.append(s[i])
        print("array is", arr)
        return "".join(arr)