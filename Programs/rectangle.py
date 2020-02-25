
# Prints a reactangle of user specified dimensions
# Batandwa mgutsi
# 25/02/2020

height = eval(input("Please enter the height: "))
width = eval(input("Please enter the width: "))
ch = input("Please enter the paint character: ")

for row in range(height):
    for column in range(width):
        if row < height//2 and column < width//2:
            print(" * ", end="")
        else:
            print(f" {ch} ", end="")
    print() # Force a newline after printing a row