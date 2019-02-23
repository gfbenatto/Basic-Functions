import random

def shuffle(word):
    w = list(word)
    random.shuffle(w)
    return ''.join(w)

print(shuffle('torlax'))