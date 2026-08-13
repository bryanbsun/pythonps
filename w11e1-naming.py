# 
# Python Problem Solver
# Week 11 Example 1: Naming Species
#

def left(string, num):
    return string[:num]

def right(string, num):
    return string[-num:]

def substr(string, start, num):
    return string[start:start+num]

str1 = input("Input a string: ")
n = int(input("Input number of characters: "))

str2 = left(str1, n)
print(f"left({str1},{n}) = {str2}")
str2 = right(str1, n)
print(f"right({str1},{n}) = {str2}")
s = int(input("Start position for substr: "))
str2 = substr(str1, s, n)
print(f"substr({str1},{s},{n}) = {str2}")
