# Calculates the volume of a cylinder- Assignment 5.
# Batandwa Mgutsi
# 10/05/2020

import math


def circle_area(diameter):
    """Returns the area of a circle with a diameter of diameter."""
    return 1/4*math.pi*(diameter**2)


def cylinder_volume(diameter, height):
    """Returns the volume of cylinder with the given diamter and height."""
    return circle_area(diameter)*height


def main():
    diameter = eval(input('Enter diameter:\n'))
    height = eval(input('Enter height:\n'))
    print('The volume of the cylinder is', '{0:.2f}'.format(
        cylinder_volume(diameter, height)))


if __name__ == '__main__':
    main()
