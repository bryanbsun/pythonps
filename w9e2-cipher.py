# 
# Python Problem Solver
# Week 9 Example 2: The Vigenere Cipher
#

N = int(input().strip())
line = input().strip()
newlist = []
answer = 0

for i in range(0,N):
    if line[i] == "?":
        if i == 0:
            newlist.append(line[i+1])
        else:
            newlist.append(line[i-1])
    else:
        newlist.append(line[i])

for i in range(0,N-1):
    if newlist[i] == newlist[i+1]:
        answer += 1

print(answer)
