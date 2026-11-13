def convert(number):
    drop_sound = ''
    if(number % 3 == 0):
        drop_sound += 'Pling'
        if(number % 5 == 0):
            drop_sound += 'Plang'
            if(number % 7 == 0):
                drop_sound += 'Plong'
                return drop_sound
            else:
                return drop_sound
        elif(number % 7 == 0):
            drop_sound += 'Plong'
            return drop_sound
        else:
            return drop_sound
    elif(number % 5 == 0):
        drop_sound += 'Plang'
        if(number % 7 == 0):
            drop_sound += 'Plong'
            return drop_sound
        else:
            return drop_sound
    elif(number % 7 == 0):
        drop_sound += 'Plong'
        return drop_sound
    else:
        return str(number)
        
        
    pass
