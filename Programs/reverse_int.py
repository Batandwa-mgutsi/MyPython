
# Reverses an integer given by the user
# Batandwa Mgutsi
# 26/02/2020

# e.g given 98 the program should print 89
# 98 % 10 = 8
# 98 // 10 = 9
#
# continuing:
# 9 % 10 = 9 terminate

num = eval(input("Please enter a number to print it in reverse: "))
print("The number in reverse is ", end='')

while num >= 10:
    # This loop will print all the digits in num from the last
    # to the 2nd digit. It won't print the first digit.

    # Print the last digit in num
    print(num % 10, end='')

    # Discard the last digit in num
    num //= 10
else:
    # Print the first digit of num
    print(num, end='')
