
# Simple calculator
# Batandwa Mgutsi
# 20/02/2020

def calculate(x, y, p):
    if(p == 'a'):
        return x+y
    elif p == 's':
        return x-y
    elif p == 'm':
        return x*y
    elif p == 'd':
        return 'Error!!!!!!' if y == 0 else x/y

x = eval(input("Enter x: "))
y = eval(input("Enter y: "))
p = input("Enter p: ")

answer = calculate(x, y, p)
print("Answer is:", answer)