N = int(input("input the number of interations: "))

sum = 0
for n in range(1, N+1):
    if n%2 != 0:
        sum += 1/(2*n-1)
    else:
        sum -= 1/(2*n-1)

answer = 4 * sum
print(f"The {N}-th proximation of Pi is {answer}")
