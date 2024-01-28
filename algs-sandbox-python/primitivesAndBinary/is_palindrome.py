def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    elif x == 0:
        return True
    elif x % 10 == 0:
        return False
    # to get last digit, mod 10
    digits = []
    while x > 0: 
        digits.append(x % 10)
        x = x // 10
    # check digits array from both ends
    i, j = 0, len(digits) - 1
    while i < j:
        if digits[i] != digits[j]:
            return False
        i += 1
        j -= 1
    # if we get here, it's a palindrome
    return True

def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(-121) == False
    assert is_palindrome(10) == False
    assert is_palindrome(-101) == False
    assert is_palindrome(0) == True


test_is_palindrome()