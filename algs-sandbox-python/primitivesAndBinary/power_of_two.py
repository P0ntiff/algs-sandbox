

"""
Given a non-negative integer, return true if the number is a power of two, return false otherwise.

"""

def power_of_two(x): 
    # 8
    # 00001000
    # 6
    # 00000110
    # powers of two are where only 1 bit is set
    num_bits_set = 0
    while x > 0:
        if (x & 1):
            num_bits_set += 1
        x >> 1
    return num_bits_set == 1



assert power_of_two(1) == True
assert power_of_two(8) == True
assert power_of_two(0) == False
assert power_of_two(0) == False