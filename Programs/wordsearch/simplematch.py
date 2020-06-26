# Program to check if a given word matches the given pattern
# Batandwa Mgutsi
# 20/06/2020

# The '?' wildcard matches any character at the corresponsing position of the word.
# Examples:
#   l?ad matches lead, load, etc
#   but does not match led or lid.


def match(patternSuffix: str, wordSuffix: str):
    """Returns False if patternSuffix[0] does not match wordSuffix[0].

        A match is when patternSuffix[0] == '?' or patternSuffix[0] == wordSuffix[0].
        This function recures until both or one of the two inputs are exhausted or a match
        of patternSuffix[0] to wordSuffix[0] is false.
    """
    if len(patternSuffix) == 0 and len(wordSuffix) == 0:
        # The inputs are exhausted
        return True

    try:
        matches = patternSuffix[0] == '?' or patternSuffix[0] == wordSuffix[0]
        if matches:
            # There is still more characters to check
            return match(patternSuffix[1:], wordSuffix[1:])
        else:
            return False
    except IndexError:
        # The two inputs are not of equal length, and therefore cannot match
        return False
