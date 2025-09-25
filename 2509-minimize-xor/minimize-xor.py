class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bitnum = bin(num2).count('1')  # Count set bits in num2
        x = 0

        # Set bits in x based on the bits of num1, from most significant to least significant
        for i in range(31, -1, -1):  # Iterate over 32 bits
            if bitnum == 0:  # Stop if all required bits are set
                break
            if num1 & (1 << i):  # Check if the i-th bit in num1 is set
                x |= (1 << i)  # Set the i-th bit in x
                bitnum -= 1  # Decrease the count of remaining bits to set

        # If there are still bits to set, set them in the least significant positions
        for i in range(32):
            if bitnum == 0:  # Stop if all required bits are set
                break
            if not (x & (1 << i)):  # Check if the i-th bit in x is not set
                x |= (1 << i)  # Set the i-th bit in x
                bitnum -= 1  # Decrease the count of remaining bits to set

        return x
