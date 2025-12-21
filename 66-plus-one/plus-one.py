class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                return digits
            digits[i] = 0
        return [1] + digits

# [9,9,9,9,9,9,9]



# a) Considering all the values are 9.
# b) Considering the last digit is not 9.
# c) Considering the last digit is 9.