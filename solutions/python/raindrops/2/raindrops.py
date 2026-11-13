def convert(number):
    drop_sound = ''

    if((number % 3 == 0) or (number % 5 == 0) or (number % 7 == 0)):
        if((number % 3 == 0) and (number % 5 == 0) and (number % 7 == 0)):
            drop_sound = "PlingPlangPlong"
            return drop_sound
        elif((number % 3 == 0) and (number % 5 == 0)):
            drop_sound = "PlingPlang"
            return drop_sound
        elif((number % 3 == 0) and (number % 7 == 0)):
            drop_sound = "PlingPlong"
            return drop_sound
        elif((number % 5 == 0) and (number % 7 == 0)):
            drop_sound = "PlangPlong"
            return drop_sound
        elif(number % 3 == 0):
            drop_sound = "Pling"
            return drop_sound
        elif(number % 5 == 0):
            drop_sound = "Plang"
            return drop_sound
        elif(number % 7 == 0):
            drop_sound = "Plong"
            return drop_sound
        else:
            pass
    else:
        return str(number)
        
        
    pass
