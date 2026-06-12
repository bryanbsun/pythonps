# 
# Python Problem Solver
# Week 6 Example 1: World Population in 2025
#

year = 2025
population = 8_230_000_000

while population < 10_000_000_000:
    population *= 1.01
    year += 1

print(f"By year {year}, world population will be {int(population):,}")

