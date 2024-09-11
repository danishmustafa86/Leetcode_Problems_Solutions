class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        st = list(bin(start)[2:])
        go = list(bin(goal)[2:])
        print(st,"how ar.e you",  go)
        while len(st) != len(go):
            if len(st) < len(go):
                st.insert(0,"0")
            elif len(go) < len(st):
                go.insert(0,"0")
        print(st,"how ar.e you",  go)

        count = 0
        for i in range(len(st)):
            if st[i] != go[i]:
                count += 1

        return count
