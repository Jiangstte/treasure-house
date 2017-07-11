def cpy_yici(stuff):
    """this function will break up words for us."""
    words = stuff.split(' ')
    return words


def cpy_erci(words):
    """sorts the words."""
    return sorted(words)


def cpy_sanci(words):
    """prints the first word after popping it off."""
    word = word.pop(0)
    print word


def cpy_sici(words):
    """prints the last word after popping it off."""
    word = words.pop(-1)
    print word


def cpy_wuci(sentence):
    """takes in a full sentence and returns the sorted words."""
    words = cpy_yici(sentence)
    return cpy_erci(words)


def cpy_liuci(sentence):
    """prints the first and last words of the sentence."""
    words = cpy_yici(sentence)
    cpy_sanci(words)
    cpy_sici(words)


def cpy_qici(sentence):
    """sorts the words then prints the first and last one."""
    words = cpy_wuci(sentence)
    cpy_sanci(words)
    cpy_sici(words)
