deck = ["G+1", "L*2","B-4","L+2","G+3","G+5","B-6","L+2","G+1","B-2"]

draws = 10
bank = 10

while draws > 0:
    draws -= 1
    card = deck[0]
    del(deck[0])
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

