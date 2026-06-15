code = int(input("Input a 6-digit number: "))
found = False
for i in range(65, 91):
    for j in range(65, 91):
        for k in range(65, 91):
            product = i * j * k
            if product == code:
                print(f"Cracked the code: {chr(i)}{chr(j)}{chr(k)}")
                found = True
                break

if not found:
    print("There no combination that matches the code!")

