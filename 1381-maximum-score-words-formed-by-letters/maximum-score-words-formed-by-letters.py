class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def is_in_letters(word, letters_cnt ):
            word_cnt = Counter(word)
            for c in word_cnt:
                if word_cnt[c] > letters_cnt[c]:
                    return False
            return True

        def cur_score(word):
            res = 0
            for c in word:
                res += score[ord(c) - ord("a")]
            return res
                
        letters_cnt = Counter(letters)
        def dfs(i):
            if i == len(words):
                return 0
            res = dfs(i + 1)
            if is_in_letters(words[i], letters_cnt):
                for c in words[i]:
                    letters_cnt[c] -= 1
                res = max(res, cur_score(words[i]) + dfs(i+1))
                for c in words[i]:
                    letters_cnt[c] += 1
            return res
        return dfs(0)

