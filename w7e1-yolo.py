# 
# Python Problem Solver
# Week 7 Example 1: YOLO
#

line = input()
# Split input into a list of words in list2
list1 = line.split()
# list2 is used for output
list2 = []

for word in list1:
    # For each word in list1, append its 1st character to the end of list2
    list2.append(word[0])

# Join all the "1st characters" into 1 string and conver to upper case
print("".join(list2).upper())
