def flip_name(s):
    if len(s) <= 1:
        return s

    return flip_name(s[1:] + s[0])