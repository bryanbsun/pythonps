def multiply(*numbers):
    print(len(numbers))
    result = 1
    for n in list(numbers):
        result *= n
    return result 
    
l = map(int, input().strip().split())
print(l)
print(*l)
print(multiply(*l))
