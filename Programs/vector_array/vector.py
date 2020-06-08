# A simple vector calculator
# Batandwa Mgutsi
# 08/06/2020

import vectormaths


def vectorize(input: str):
    """The input should be 3 bumbers seperated by spaces
    Returns a list of floats"""
    array = input.split(' ')
    return [
        eval(array[0]),
        eval(array[1]),
        eval(array[2]),
    ]


A = vectorize(input('Enter vector A:\n'))
B = vectorize(input('Enter vector B:\n'))
operator = input("Select a calculation to perform. Enter '+', '.' or '|':\n")

if operator == '+':
    print(f'A+B = {vectormaths.vector_sum(A, B)}')
elif operator == '.':
    print(f'A.B = {vectormaths.vector_product(A, B)}')
elif operator == '|':
    normA = vectormaths.vector_norm(A)
    normB = vectormaths.vector_norm(B)
    print('|A| = {:.2f}'.format(normA))
    print('|B| = {:.2f}'.format(normB))
else:
    print('Selection not recognised')
