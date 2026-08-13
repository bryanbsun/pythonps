# 
# Python Problem Solver
# Week 11 Problem 2: Smart Blender
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

def smart_blend(name1, name2):
    n1 = length(name1)
    n2 = length(name2)
    for i in range(1, n1 + 1):
        first_fragment = left(name1, i)
        seam = right(first_fragment, 1)          # last letter of the first fragment
        for j in range(0, n2):
            if substr(name2, j, 1) == seam:      # a matching letter in name2
                tail = substr(name2, j + 1, n2 - (j + 1))
                return concat(first_fragment, tail)   # keeps one copy of the seam
    return blend(name1, name2)                    # no seam -> plain blend

str1, str2 = map(str, input("Input names of 2 species: ").split()) 
print(smart_blend(str1, str2))
