# 
# Python Problem Solver
# Week 14 Example 1: Email Address Validator
#

def validate_email():
    # Step 1: Input a string
    email = input("Enter an email address: ")

    # Step 2: Scan for "@" signs and count them
    at_count = email.count('@')
    if at_count != 1:
        print("Invalid: email must contain exactly one '@' sign.")
        return
    at_pos = email.index('@')

    # Step 3: Scan for "." before and after the "@"
    #   The rules require at least one "." AFTER the "@".
    dot_after = '.' in email[at_pos + 1:]
    if not dot_after:
        print("Invalid: email must contain a '.' after the '@' sign.")
        return

    # Step 4: Scan for invalid characters (spaces and "#")

    #if " " in email or "#" in email:
    for ch in email:
        if ch == ' ' or ch == '#':
            print("Invalid: email cannot contain spaces or '#' signs.")
            return

    # Step 5: Check "@" position and its relative position with "."
    #   - "@" cannot be first
    #   - at least 1 character between "@" and the next "."
    if at_pos == 0:
        print("Invalid: '@' cannot be in the first position.")
        return
    next_dot = email.index('.', at_pos + 1)   # first "." after the "@"
    if next_dot - at_pos < 2:                 # e.g. "a@.com" -> nothing between
        print("Invalid: there must be at least 1 character between '@' and '.'.")
        return

    # Step 6: Check "." position (cannot end with ".")
    if email.endswith('.'):
        print("Invalid: email cannot end with a '.' sign.")
        return

    # Step 7: Confirm valid
    print("Valid email address.")


validate_email()
