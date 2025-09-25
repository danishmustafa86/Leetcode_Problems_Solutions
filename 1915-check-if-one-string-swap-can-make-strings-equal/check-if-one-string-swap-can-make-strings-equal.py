class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        s1_list = list(s1)

        for i in range(len(s1)):
            for j in range(i, len(s1)):
                cur1 = s1_list.copy()
                cur1[i], cur1[j] = cur1[j], cur1[i]
                cur1 = "".join(cur1)
                
                if cur1 == s2:
                    return True


        return False