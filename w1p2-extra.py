# 
# Python Problem Solver
# Week 1 Problem 2: Safety Butffer
#

# Initialise mission data

crew2 = 4
crew3 = 4
crew4 = 6
crew5 = 8
days2 = 10
days3 = 30
days4 = 45
days5 = 60
oxpd = 5
fdpd = 3
maxox1 = 800
maxox2 = 1200
maxox3 = 2400
maxfd1 = 500
maxfd2 = 800
maxfd3 = 1800

# Get user choice of ship and mission
# Keep asking if input not valid

ship = int(input("Choose a ship (1-Orion, 2-Space Voyager, 3-Deep Space Explorer): "))
while ship < 1 or ship > 3:
    ship = int(input("Choose a ship (1-Orion, 2-Space Voyager, 3-Deep Space Explorer): "))

mission = int(input("Enter a mission number: "))
while mission < 2 or mission > 5:
    mission = int(input("Enter a mission number: "))

# Calculate maximum oxygen and food capacity
if ship == 1:
    shipname = "Orion"
    maxfd = maxfd1
    maxox = maxox1
elif ship == 2:
    shipname = "Space Voyager"
    maxfd = maxfd2
    maxox = maxox2
elif ship == 3:
    shipname = "Deep Space Explorer"
    maxfd = maxfd3
    maxox = maxox3

# Calculate total oxygen and food consumption

if mission == 2:
    missionname = "Artemis II"
    crew = crew2
    days = days2
elif mission == 3:
    missionname = "Artemis III"
    crew = crew3
    days = days3
elif mission == 4:
    missionname = "Artemis IV"
    crew = crew4
    days = days4
elif mission == 5:
    missionname = "Artemis V"
    crew = crew5
    days = days5

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
print(f"Spaceship: {shipname}")
print(f"Crew: {crew}")
print(f"Days: {days}")
print(f"Oxygen needed: {totalox} units")
print(f"Food needed: {totalfd} units")
if safe:
    print("Status: READY FOR LAUNCH")
else:
    print("Status: NOT SAFE TO LAUNCH")


