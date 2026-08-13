# 
# Python Problem Solver
# Week 12 Problem 2: Codenames
#

def codename(name):
    return name[:3].upper() + "-" + str(len(name))

animals = ["Wolf", "Dolphin", "Koala", "Owl"]
codes = list(map(codename, animals))
print(codes)          # ['WOL-4', 'DOL-7', 'KOA-5', 'OWL-3']
