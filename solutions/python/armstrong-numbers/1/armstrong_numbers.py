def is_armstrong_number(number):
    num_str = str(number)
    num_len = len(num_str)
    
    total = 0
    i = 1

    while i <= num_len:
        str_value = num_str[i-1]

        num_value = int(str_value)
        total = total + (num_value ** num_len)

        i += 1
    
    if (total != number):
        return False
    else:
        return True