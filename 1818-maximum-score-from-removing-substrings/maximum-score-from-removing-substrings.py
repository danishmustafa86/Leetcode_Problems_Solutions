class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_and_score(s: str, first: str, second: str, score: int) -> (str, int):
            stack = []
            current_score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    current_score += score
                else:
                    stack.append(char)
            return ''.join(stack), current_score

        if x > y:
            s, score1 = remove_and_score(s, 'a', 'b', x)
            s, score2 = remove_and_score(s, 'b', 'a', y)
        else:
            s, score1 = remove_and_score(s, 'b', 'a', y)
            s, score2 = remove_and_score(s, 'a', 'b', x)
        
        return score1 + score2
