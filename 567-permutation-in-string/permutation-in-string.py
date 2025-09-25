class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1count = [0] * 26
        s2count = [0] * 26
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord("a")] += 1
            s2count[ord(s2[i]) - ord("a")] += 1

        if s1count == s2count :
            return True
        for i in range(len(s1), len(s2)):
            s2count[ord(s2[i]) - ord("a")] += 1
            s2count[ord(s2[i - len(s1)]) - ord("a")] -= 1
        
            if s1count == s2count:
                return True
        return False
















        # l1 = list(s1)
        # l1.sort()
        # k = len(l1)
        
        # for i in range(len(s2)-k+1):
        #     var = list(s2[i:i+k])
        #     var.sort()
        #     if var == l1:
        #         return True
        # return False








        