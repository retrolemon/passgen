from random import choice

def passgen(length, charset):
    res = []
    for i in range(length):
        res.append(choice(charset))
    res = "".join(res)
    return(res)
