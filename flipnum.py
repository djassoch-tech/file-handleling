def flip_number(n):
    if n<10:
        return n

    last_digit = n % 10

    remaining = n //10

    digits = len(str(remaining))

    return last_digit * ( 10 **digits) + flip_number(remaining)

flip_number(324)