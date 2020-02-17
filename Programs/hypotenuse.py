
# Prints the length of the hypotenuse of a right angled triangle
# Batandwa Mgutsi
# 17/02/2020

from math import sqrt
from math import pow

# We can also simpy say:
#  import math
# In this case you must prefix all calls to this module with math.
# e.g math.sqrt()

x = eval(input("Please enter the first short side: "))
y = eval(input("Please enter the 2nd short side: "))

answer = round(sqrt(x**2 + y**2), 2)
print("The length of the hypotenuse is: ", answer)