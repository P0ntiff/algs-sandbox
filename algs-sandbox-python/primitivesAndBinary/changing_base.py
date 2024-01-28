"""
Given an integer represented as a string under base b1, convert it to base b2 and return it as a string.

Input-Output

Example 1

Input: ("12", 10, 2)
Output: "1100"
Explanation: We are converting "12" which is under base 10 (decimal) to base 2 (binary)
Constraints

2 <= b1 <= 36
2 <= b2 <= 36
For base 2 to base 10 use digits 0-9 to represent digits
For base 11 to base 36 use alphabet characters A-Z to represent digits (case insensitive)
"""

def changing_base(input: str, b1: int, b2: int):
    if (b1 == b2):
        return input
    isNegative = input[0] == "-"
    
    maxPower = len(input) - 1
    startIndex = 0
    if (isNegative):
        startIndex = 1
    
    # convert from b1 to integer intermediary
    numAsInteger = 0
    # 12
    # 1 * 12^1 + 2 * 12^0
    for i in range(startIndex, len(input)):
        positionValue = char_to_place_value(input[i], b1)
        power = maxPower - i
        numAsInteger += positionValue * b1**power

    # output in b2 format
    if (numAsInteger == 0):
        return 0
    else:
        output = ""
        while (numAsInteger > 0):
            remainder = numAsInteger % b2
            numAsInteger = numAsInteger // b2
            output = place_value_to_char(remainder) + output
        return "-" + output if isNegative else output

def char_to_place_value(digit: str, base:int):
    if (is_number(digit)):
        return int(digit)
    else:
        return ord(digit) - 55

def place_value_to_char(digit: int):
    if (digit < 10):
        return str(digit)
    else:
        return chr(digit + 55)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def test_changing_base():
    # Test conversion from base 10 to base 2
    assert changing_base("12", 10, 2) == "1100"

    # Test conversion from base 2 to base 10
    assert changing_base("1100", 2, 10) == "12"

    # Test conversion from base 16 to base 8
    assert changing_base("1F", 16, 8) == "37"

    # Test conversion from base 36 to base 36 (identity test)
    assert changing_base("XYZ", 36, 36) == "XYZ"


test_changing_base()