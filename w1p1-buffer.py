# 
# Python Problem Solver
# Week 1 Problem 2: Safety Butffer
#

# Initialise mission data

crew2 = 4
crew3 = 4
days2 = 10
days3 = 30
oxpd = 5
fdpd = 3
maxox = 800
maxfd = 500

# Get user choice of mission
# Keep asking if input not valid

mission = int(input("Enter a mission number: "))
while mission != 2 and mission != 3:
    mission = int(input("Enter a mission number: "))

# Calculate total oxygen and food consumption

if mission == 2:
    missionname = "Artemis II"
    crew = crew2
    days = days2
elif mission == 3:
    missionname = "Artemis III"
    crew = crew3
    days = days3

totalox = crew * days * oxpd
totalfd = crew * days * fdpd

# Decide whether it's safe to launch

if totalox * 1.15 <= maxox and totalfd * 1.15 <= maxfd:
    safe = True
    print("+--------------------------+")
    print("|     READY FOR LAUNCH!    |")
    print("+--------------------------+")
else:
    safe = False
    print("+--------------------------+")
    print("|   NOT SAFE TO LAUNCH!    |")
    print("+--------------------------+")

# Print mission report

print(f"Mission: {missionname}")
print("Spaceship: Orion")
print(f"Crew: {crew}")
print(f"Days: {days}")
print(f"Oxygen needed: {totalox} units")
print(f"Food needed: {totalfd} units")
if safe:
    print("Status: READY FOR LAUNCH")
else:
    print("Status: NOT SAFE TO LAUNCH")


