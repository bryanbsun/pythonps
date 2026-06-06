# 
# Python Problem Solver
# Week 5 Example 3: Uno Bank
#

# Generate a deck
deck = ["G+1", "G+5", "L*2", "B-4", "L+2", "G+3", "G+5", "B-6", "L/2", "G+1", "B-2", "G+3"]

draws = 10
bank = 10

# Keep drawing until no draw left
while draws > 0:
    # Draw 1
    draws -= 1

    # Draw 1 card from the deck, and remove it from the deck
    card = deck[0]
    del(deck[0])

    # Take actions according to card drawn
    if card[0] == 'G':
        bank += int(card[2])
    elif card[0] == 'B':
        bank -= int(card[2])
    elif card[0] == 'L':
        if card[1] == '+':
            draws += int(card[2])
        elif card[1] == '-':
            draws -= int(card[2])
        elif card[1] == '*':
            bank *= int(card[2])
        elif card[1] == '/':
            bank //= int(card[2])

print(f"Your final bank account balance is {bank}.")
