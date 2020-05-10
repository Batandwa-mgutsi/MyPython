# A program that simulates a vending machine.
# Batandwa Mgutsi
# 01/05/2020

cost = eval(input('Enter the cost (in Rand):\n'))

deposit = 0
while deposit < cost:
    deposit += eval(input('Deposit a coin or note (in Rand):\n'))

change = deposit - cost

# Find the right notes to give to the user for change

changeNotes = {
    50: 0,
    20: 0,
    10: 0,
    5: 0,
    2: 0,
    1: 0,
}

while change > 0:
    biggerNote = 0
    for note in changeNotes:
        # Get the biggest note as part of the change
        if change >= note and biggerNote < note:
            biggerNote = note
    change -= biggerNote
    changeNotes[biggerNote] += 1

# Give the change to the user, ignore the note we did'nt calculate to be part of the change.
print('Your change is:')
for note in changeNotes:
    if changeNotes[note] != 0:
        print(changeNotes[note], 'x', f'R{note}')
