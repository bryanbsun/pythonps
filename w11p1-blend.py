# 
# Python Problem Solver
# Week 11 Problem 1: Name Blender
#

def left(string, num):
    return string[:num]

def right(string, num):
    return string[-num:]

def substr(string, start, num):
    return string[start:start+num]

def length(string):
    return len(string)

def concat(string1, string2):
    return string1+string2

def blend(name1, name2):
    left_count  = (length(name1) + 1) // 2   # left half, rounded up
    right_count = (length(name2) + 1) // 2   # right half, rounded up
    return concat(left(name1, left_count), right(name2, right_count))

str1, str2 = map(str, input("Input names of 2 species: ").split()) 
print(blend(str1, str2))
