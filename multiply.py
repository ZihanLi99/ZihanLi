def multiply(a,b):
    """
    Returns the greatest common divisor of a and b
    """
    if b == 0:
        return 0
    else:
        return a + multiply(a, b - 1)

print(multiply(7,4))
