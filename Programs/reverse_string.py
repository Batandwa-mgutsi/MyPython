
# Prints the given out in reverse
# Batandwa Mgutsi
# 02/03/2020

sentence = input("Please enter a sentence:\n")

print("The string in reverse is: ", end="")
for i in range(len(sentence), 0, -1):
    print(sentence[i-1], end='')
