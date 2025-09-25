class Solution:
    def minOperations(self, logs: List[str]) -> int:
        var = 0
        for i in range(len(logs)):
            if logs[i] == "../" and var !=0:
                var -= 1
            elif logs[i] == "./":
                var += 0
            else:
                if logs[i] == "../" and var ==0:
                    var += 0
                else:
                    var += 1

        return var



