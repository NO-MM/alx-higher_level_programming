#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exeption["Too far"]
            else:
                result += a ** b / i
        except Exeption:
            result = b + a
            break
    return result
