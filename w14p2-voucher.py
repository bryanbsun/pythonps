# 
# Python Problem Solver
# Week 14 Problem 2: Discount Vouchers
#

def is_valid_voucher(code):
    # Rule 3: no spaces or "*" anywhere
    if ' ' in code or '*' in code:
        return False

    # Rule 1: exactly one "-"
    if code.count('-') != 1:
        return False

    hyphen_pos = code.index('-')

    # Rule 4a: "-" cannot be first (at least 1 char before it)
    if hyphen_pos == 0:
        return False

    # Rule 5: cannot end with "-"
    if code.endswith('-'):
        return False

    # Rule 2: at least one digit after the "-"
    after = code[hyphen_pos + 1:]
    if not any(ch.isdigit() for ch in after):
        return False

    return True


# quick checks
tests = [
    "SUMMER-2025",   # valid
    "A-1",           # valid (one char before, one digit after)
    "-2025",         # hyphen first
    "SUMMER-",       # ends with hyphen / no digit after
    "SUMMER-SALE",   # no digit after hyphen
    "SUM-MER-25",    # two hyphens
    "SUMMER 2025",   # space
    "SUMMER*2025",   # asterisk
]
for t in tests:
    print(f"{t:15} -> {is_valid_voucher(t)}")
