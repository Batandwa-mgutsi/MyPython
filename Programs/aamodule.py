# A module for filtering a string
# Batandwa Mgutsi
# 28/05/2020


def doSingleFilter(s, t1):
    output = ''
    for character in s:
        if (t1 == 'l'):
            if not character.isalpha():
                output += character
        elif (t1 == 'd'):
            if not character.isdigit():
                output += character
        elif (t1 == 'o'):
            if character.isalpha() or character.isdigit():
                output += character
    return output


def filter(s, t):
    output = s
    for t1 in t:
        output = doSingleFilter(output, t1)
    return output


if __name__ == '__main__':
    print(filter('55 bottles of beer', 'do'))
    print(filter('55 bottles of beer', 'o'))
    print(filter('55 bottles of beer', 'l'))
    print(filter('55 bottles of beer', 'dl'))
