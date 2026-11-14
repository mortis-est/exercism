def square(number):
    if(number >= 1) and (number <= 64):
        return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")
    
    pass


def total():
    i = 1
    total = 0
    while i <= 64:
        total = total + (2 ** (i - 1))
        i += 1
    return total
    pass
