def is_power4(n):
    if n ==1:
        return True
    if n <= 0 or n % 4 != 0:
        return False

    return is_power4(n//4)