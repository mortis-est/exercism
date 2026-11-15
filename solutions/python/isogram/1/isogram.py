def is_isogram(phrase):
    phrase = phrase.replace("-", "")
    phrase = phrase.strip()
    phrase = phrase.lower()
    phrase = ''.join(phrase.split())


    if len(phrase) == len(set(phrase)):
        return True
    else:
        return False
    pass
