# A program that draws the curve of the function given by the user.
# Batandwa Mgutsi
# 02/05/2020

import math


def getPointIndex(x, y, pointsPerWidth, pointsPerHeight):
    """Returns the index of the given point in a poinsPerWidth*pointsPerHeight grid.
       pointsPerWidth and pointsPerHeight should be odd numbers"""
    # These calculations take the top left corner as the (0;0) point
    # and both axes increase from that point.
    originRow = int(pointsPerHeight/2)
    originColumn = int(pointsPerWidth/2)

    # A positive x value increases the column, and vice versa
    # A positive y value decrease the row since the above calculations took the row as increasing
    # when going downwards.
    pointRow = originRow - y
    pointColumn = originColumn + x
    index = pointRow*pointsPerWidth+pointColumn
    return index


def printGraph(graph, pointsPerWidth, pointsPerHeight):
    for row in range(pointsPerHeight):
        for column in range(pointsPerWidth):
            print(graph[row*pointsPerWidth+column], end='')
        print()


def drawCurve(function, graph, pointsPerWidth, pointsPerHeight, fill='o'):
    output = list(graph)
    halfOfXAxis = int(pointsPerWidth/2)
    for x in range(-halfOfXAxis, halfOfXAxis+1):
        try:
            # Using a try/except will prevent the program from crashing in case an error occurs while
            # evaluating the function at the current x value. For example, if the function is a hyperbola
            # the try/except will prevent the program from crashing when x is an asymptote of the function.
            y = eval(function)
        except:
            continue
        y = round(y)
        pointIndex = getPointIndex(x, y, pointsPerWidth, pointsPerHeight)
        if pointIndex < 0 or pointIndex >= len(buffer):
            continue
        else:
            output[pointIndex] = fill

    return output


# Using a grid with [-10, 10] endpoints
buffer = list(''.rjust(21*21))

# Draw the axes
for y in range(-10, 11):
    buffer[getPointIndex(0, y, 21, 21)] = '|'
buffer = drawCurve('0', buffer, 21, 21, '-')
buffer[getPointIndex(0, 0, 21, 21)] = '+'


function = input('Enter a function f(x):\n')
buffer = drawCurve(function, buffer, 21, 21)
printGraph(buffer, 21, 21)
