def equilateral(sides):
    sides = sorted(sides)
    if((sides[0] + sides [1]) < sides[2]):
        return False
    if((sides[0] <= 0) or (sides[1] <= 0) or (sides[2] <= 0)):
        return False
    elif((sides[0] == sides[1]) and (sides[0] == sides[2])):
        return True
    else:
        return False
    pass


def isosceles(sides):
    sides = sorted(sides)
    if((sides[0] + sides [1]) < sides[2]):
        return False
    if((sides[0] <= 0) or (sides[1] <= 0) or (sides[2] <= 0)):
        return False
    elif((sides[0] == sides[1]) or (sides[0] == sides[2]) or (sides[1] == sides[2])):
        return True
    else:
        return False
    pass
def scalene(sides):
    sides = sorted(sides)
    if((sides[0] + sides [1]) < sides[2]):
        return False
    if((sides[0] <= 0) or (sides[1] <= 0) or (sides[2] <= 0)):
        return False
    elif((sides[0] != sides[1]) and (sides[1] != sides[2]) and (sides[2] != sides[0])):
        return True
    else:
        return False
