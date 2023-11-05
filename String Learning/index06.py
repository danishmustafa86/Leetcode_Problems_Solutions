class Solution:
    def arrayStringsAreEqual(self, word1: ["ab", "c"], word2: ["a", "bc"]) -> bool:
        n1="".join(word1)
        n2="".join(word2)
        if n1==n2:
            return True
    
        return False
