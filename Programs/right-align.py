# A program that takes a list of strings as input and right aligns
# them by the longest of the strings.
# Batandwa Mgutsi
# 08/06/2020

words = []
longestLength = 0

print('Enter strings (end with DONE):')
while True:
    wordInput = input()
    if wordInput == 'DONE':
        break
    else:
        words.append(wordInput)
        if len(wordInput) > longestLength:
            longestLength = len(wordInput)

# Now align them to the right and print them
print('Right-aligned list:')
for iii in range(len(words)):
    wordInput = words[iii]
    numberOfSpaces = longestLength - len(wordInput)
    print(' ' * numberOfSpaces+wordInput)
