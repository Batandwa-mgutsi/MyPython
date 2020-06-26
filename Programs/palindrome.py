# Using recursion, checks if the user given string is palidrome or not.
# Batandwa Mgutsi
# 25/06/2020


def checkLocator(subject: str, locator: int):
    """Returns False if the character at subject[locator] is not equal to its counterpart at
    subject[-locator-1].

    locator is the zero starting index of the current character to be checked.
    This method recurs with incrementing locator until all characters in subject have been checked with
    their counterparts, at which case True will be returned.

    subject should have an even length. In an odd length string, one character will not have a counterpart
    and an IndexError might be raised.
    """
    if locator == len(subject) // 2:
        return True

    if subject[locator] != subject[-locator-1]:
        return False
    else:
        return checkLocator(subject, locator+1)


def isPalidrome(subject: str):
    """Returns True if subject is a palidrome string, False otherwise."""

    inputLength = len(subject)
    if(inputLength < 2):
        return True

    # Ignore the single mid character in odd length input
    if inputLength % 2 != 0:
        subject = subject[0:inputLength//2] + subject[inputLength//2+1:]

    return checkLocator(subject.lower(), 0)


def test():
    assert checkLocator("Good", 2) == True
    assert checkLocator("Good", 0) == False
    assert checkLocator("anna", 0) == True

    assert isPalidrome("Anna") == True
    assert isPalidrome("Noon") == True
    assert isPalidrome("Kayak") == True
    assert isPalidrome("able was I ere I saw elba") == True
    assert isPalidrome("elba is a noob") == False
    assert isPalidrome("Batandwa") == False
    print("All tests passed")


if __name__ == "__main__":
    subject = input("Enter a string:\n")
    if isPalidrome(subject):
        print("Palindrome!")
    else:
        print("Not a palindrome!")
