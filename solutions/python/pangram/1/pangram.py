def is_pangram(sentence):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    sentence = sentence.lower()
    return all(letter in sentence for letter in letters)
    pass
