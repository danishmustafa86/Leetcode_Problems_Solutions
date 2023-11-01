class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        halve1 = s[:len(s) // 2]
        halve2 = s[len(s) // 2:]
        leftside = 0
        rightside = 0

        for i in range(len(halve1)):
            if halve1[i] in vowels:
                leftside += 1
            if halve2[i] in vowels:
                rightside += 1

        return leftside == rightside
