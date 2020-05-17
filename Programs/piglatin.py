# A module for translating English to piglatin and vice-versa- Assignment 5.
# @see: http://en.wikipedia.org/wiki/Pig_Latin
# Batandwa Mgutsi
# 17/05/2020

CONST_VOWELS = ['a', 'e', 'i', 'o', 'u']


def transformEnglishToPiglatin(englishUnits: list):
    """Transforms the given english units to piglatin units."""
    # If the word begins with a vowel, ‘way’ should be appended (example: ‘apple’ becomes
    # ‘appleway’)
    # if the word begins with a sequence of consonants, this sequence should be moved to the
    # end, prefixed with ‘a’ and followed by ‘ay’ (example: ‘please’ becomes ‘easeaplay’)
    pigLatinUnits = list()

    for unit in englishUnits:
        if(len(unit) == 0):
            continue

        firstChar = unit[0]
        if firstChar in CONST_VOWELS:
            pigLatinUnits.append(unit + 'way')
            continue

        else:
            firstConsonents = ''
            for letter in unit:
                if letter in CONST_VOWELS:
                    break
                else:
                    firstConsonents += letter

            pigLatinWord = unit[len(firstConsonents)::]
            pigLatinWord += 'a' + firstConsonents+'ay'
            pigLatinUnits.append(pigLatinWord)

    return pigLatinUnits


def allConsonents(items: str):
    """Returns True if all the letters in items are consonents, False otherwise."""
    for letter in items:
        if letter in CONST_VOWELS:
            return False

    return True


def transformPiglatinToEnglish(pigLatinUnits: list):
    """Transforms the given english piglatin units to english units, i.e reverses transformEnglishToPiglatin()."""
    # Assume, when reverting Pig Latin to English that the original English text does not contain the letter "w".
    englishUnits = list()

    for unit in pigLatinUnits:
        if 'w' in unit:
            englishUnits.append(unit[0:unit.index('w')])
            continue

        if unit.endswith('ay'):
            hasLetterABeforeAy = False
            inBewteenConsonents = ''
            for index in range(unit.index('ay')-len(unit)-1, -len(unit)-1, -1):
                if unit[index] == 'a':
                    hasLetterABeforeAy = True
                    break
                else:
                    inBewteenConsonents += unit[index]

            if hasLetterABeforeAy and allConsonents(inBewteenConsonents):
                englishWord = unit[0:len(unit)-len(inBewteenConsonents)-3]
                englishUnits.append(inBewteenConsonents[len(
                    inBewteenConsonents)::-1]+englishWord)
                continue

        englishUnits.append(unit)

    return englishUnits


def to_pig_latin(sentence: str):
    units = sentence.split()
    return ' '.join(transformEnglishToPiglatin(units))


def to_english(sentence: str):
    units = sentence.split()
    return ' '.join(transformPiglatinToEnglish(units))


def main():
    pass


if __name__ == '__main__':
    main()
