class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        n1:string ="".join(word1)
        n2:string ="".join(word2)
        if n1==n2:
            return True
    
        return False
