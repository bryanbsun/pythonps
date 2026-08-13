from math import *

def left(string, num):
    return string[:num]

def right(string, num):
    return string[-num:]

def substr(string, start, num):
    return string[start:start+num]

def concat(string1, string2):
    return string1+string2

string1, string2 = map(str, input("Please input names of 2 animals: ").split())
n1 = len(string1)
n2 = len(string2)

found = False
for i in range(1, n1):
    for j in range(n2):
        if substr(string1, i, 1) == substr(string2, j, 1):
            print(concat(left(string1, i+1), right(string2, n2 - 1 - j)))
            found = True

if not found:
    print(concat(left(string1, ceil(n1/2)), right(string2, ceil(n2/2))))
