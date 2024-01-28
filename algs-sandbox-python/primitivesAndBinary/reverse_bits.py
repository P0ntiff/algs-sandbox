
def reverse_bits(n: int) -> int:
    reversed_bits = 0
    while n > 0:
        reversed_bits = (reversed_bits << 1) | (n & 1)
        n >>= 1
    return reversed_bits
