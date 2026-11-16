def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    iter = 1
    divisors = []
    aliquot_sum = 0
    
    if int(number) < 1:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        
        while iter < int(number):
            if int(number) % iter == 0:
                divisors.append(iter)
                iter += 1
            else:
                iter += 1
                continue
        for element in divisors:
            aliquot_sum += int(element)
        if int(number) == aliquot_sum:
            return "perfect"
        elif int(number) < aliquot_sum:
            return "abundant"
        elif int(number) > aliquot_sum:
            return "deficient"
        else:
            raise ValueError("wtf")

    pass
        
                