# 
# Python Problem Solver
# Week 13 Example 2: Email Address Validator
#


email = input("Enter an email address: ")
is_valid, message = validate_email(email)

# Rule 3: no spaces or "#" signs
if " " in email or "#" in email:
    return False, 'Email cannot contain spaces or "#" signs.'

# Rule 1: one and only one "@"
if email.count("@") != 1:
    return False, 'Email must contain exactly one "@" sign.'

# Rule 5: cannot end with "."
if email.endswith("."):
    return False, 'Email cannot end with a "." sign.'

# Rule 4a: "@" cannot be in the first position
at_index = email.index("@")
if at_index == 0:
    return False, 'The "@" sign cannot be in the first position.'

# Split into the part before and after the "@"
after_at = email[at_index + 1:]

# Rule 2: at least one "." located after the "@"
if "." not in after_at:
    return False, 'Email must contain a "." after the "@" sign.'

# Rule 4b: at least 1 character between "@" and the first "." after it
dot_index = after_at.index(".")
if dot_index < 1:
    return False, 'There must be at least 1 character between "@" and ".".'

return True, "Valid email"

