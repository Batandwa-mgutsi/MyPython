
# Calculates the minimum and maximum integers in python
# Batandwa Mgutsi
# 28/02/2020

def calculate(goLow):
    counter = 0
    temp = counter
    while True:
        print(counter)
        if goLow:
            temp -= 1
            if temp >= 0:
                return counter
            else:
                counter = temp
        else:
            temp += 1
            if temp <= 0:
                return counter
            else:
                counter = temp   


print("Minimum integer is ", calculate(True)) 
print("Maximum integer is", calculate(False))