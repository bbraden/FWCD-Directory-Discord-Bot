import re

def getToken():
    a = ''
    with open('token.txt') as file:
        a = file.readlines()

    a2 = str(a)
    b = "[]'"
    for char in b:
        token = a2.replace(char, "")
    res = str(token)[1:-1]
    token = res
    return token