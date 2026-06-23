# 
# Python Problem Solver
# Week 8 Example 3: How Security is Your Password
#

N = 52
L = 10

c = N**L
sec = c//1000000000
days = sec//86400
years = days//365
days -= years * 365
rsec = sec - (years * 365 + days) * 86400
hours = rsec//3600
minutes = (rsec - hours * 3600)//60
seconds = rsec - hours * 3600 - minutes * 60

print(f"The password will be cracked in {years} years, {days} days, {hours} hours, {minutes} moinutes and {seconds} seconds")
