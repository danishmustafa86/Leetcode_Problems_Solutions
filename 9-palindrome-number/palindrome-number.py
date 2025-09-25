class Solution:
    def isPalindrome(self, x: int) -> bool:
       original_no = x 
       # storing the original no for comparsion later on 
       if x < 0 : 
        return False
       counter = 0 
       while x > 0:
            counter = (counter * 10) + (x % 10)
            x = x // 10
       return original_no == counter