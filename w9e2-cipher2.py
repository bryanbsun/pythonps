# 
# Python Problem Solver
# Week 9 Example 2: The Vigenere Cipher 2
#

original = input("Input the plain text: ").strip().upper()
key = input("Input the encryption key: ").strip().upper()

keylist = []
for k in key:
    keylist.append(ord(k) - 65)
keylist *= len(original)//len(key)+1
cipher = ""

for i in range(len(original)):
    asc = ord(original[i])
    asc += keylist[i]
    if asc > 90:
        asc -= 26
    cipher += chr(asc)

print(f"The Caesar cipher of '{original}' is '{cipher}'.")

