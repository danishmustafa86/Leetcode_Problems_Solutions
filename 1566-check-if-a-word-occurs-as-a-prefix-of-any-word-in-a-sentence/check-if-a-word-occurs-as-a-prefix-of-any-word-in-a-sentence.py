class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        arr = list(sentence.split())
        for i in range(len(arr)):
            cur = arr[i]
            if len(cur) >= len(searchWord) and   searchWord == cur[:len(searchWord) ]:
                return i + 1
        return -1