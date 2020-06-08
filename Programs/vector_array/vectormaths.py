# A module for doing basic 3D vector maths
# Batandwa Mgutsi
# 08/06/2020

# A vector is an arry with 3d elements

import math


def vector_sum(A: list, B: list):
    return [
        A[0] + B[0],
        A[1] + B[1],
        A[2] + B[2],
    ]


def vector_product(A: list, B: list):
    return A[0] * B[0] + A[1] * B[1] + A[2] * B[2]


def vector_norm(A: list):
    return math.sqrt(A[0]**2 + A[1]**2 + A[2]**2)
