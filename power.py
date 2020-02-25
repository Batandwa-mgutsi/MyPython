
# Calculates a^b using a for loop
# Batandwa Mgutsi
# 25/02/2020

a = eval(input("Enter a: "))
b = eval(input("Enter b: "))

ans = 1
for _ in range(1, b+1):
    ans *= a

print(a, "to the power of ", b, "is", ans)