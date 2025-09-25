class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def r_s(s:str,first:str,second:str,score:int) -> (str,int):
            stack = []
            cur_score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    cur_score += score
                else:
                    stack.append(char)
            return "".join(stack), cur_score
        if x>y:
            s, score1 = r_s(s, "a", "b", x)
            s, score2 = r_s(s, "b", "a", y)
        else:
            s, score2 = r_s(s, "b", "a", y)
            s, score1 = r_s(s, "a", "b", x)
        return score1 + score2
