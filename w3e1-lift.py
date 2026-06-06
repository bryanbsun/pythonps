# 
# Python Problem Solver
# Week 3 Example 1: the Smart Lift
#

# Get a room number
room = int(input("Room Number : "))

# Integer divide room number by 7 to get floor.  
# Note that 7//7 is not equal to 6//7, so room - 1
floor = (room - 1) // 7

# Reject invalid room number
if room < 1 or room > 707:
    print("Invalid Room Number!")
else:
    if floor == 0:
        print("Ground Floor")
    else: 
        print(floor)
