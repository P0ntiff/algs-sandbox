def is_power_of_four(x):
    #check number is > 0
    if (x <= 0):
        return False
    # check if number is power of 4
    # 1/ should be a power of 2
    is_power_of_two = (x & (x - 1)) == 0
    # 2/ bit mask on every second bit should return original number
    power_of_four_mask = 0b0101010101010101
    if (is_power_of_two and (x & power_of_four_mask == x)):
        return True
    return False


def test_power_of_four():
    assert is_power_of_four(16) == True
    assert is_power_of_four(64) == True
    assert is_power_of_four(256) == True
    assert is_power_of_four(15) == False
    assert is_power_of_four(32) == False
    assert is_power_of_four(1024) == True
    assert is_power_of_four(0) == False
    assert is_power_of_four(-16) == False
    assert is_power_of_four(1) == True
    assert is_power_of_four(4) == True


test_power_of_four()