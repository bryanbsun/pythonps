# 
# Python Problem Solver
# Week 6 Problem 1: World in 2025
#

year = 2025
population = 8_230_000_000

for year in range (2026, 2050+1):
    population *= 1.01

print(f"By year {year}, world population will be {int(population):,}")

