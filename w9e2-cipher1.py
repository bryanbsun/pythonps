# 
# Python Problem Solver
# Week 9 Example 2: The Vigenere Cipher 1
#

original = input("Input the plain text: ").strip().upper()
key = int(input("Input the encryption key: ").strip())

cipher = ""

for c in original:
    asc = ord(c)
    asc += key
    if asc > 90:
        asc -= 26
    cipher += chr(asc)

print(f"The Caesar cipher of '{original}' is '{cipher}'.")

