# Program that prints a list of words that match a given pattern in a file
# Batandwa Mgutsi
# 20/06/2020

import simplematch


def getFileContents(fileName: str) -> list:
    """Returns the contents of a file as a list of strings, each string being a line from the file.

        None is returned on error."""
    try:
        file = open(fileName, 'r')
        contents = file.readlines()
        file.close()
        return contents
    except IOError:
        return None


def getReadablePortion(lines: list) -> list:
    """Returns the portion of lines that starts with the line with text 'START'"""
    start = lines.index('START\n')
    return lines[start:]


def getMatches(pattern: str, lines: list) -> list:
    """Returns all the lines that match the given mattern"""
    matches = []
    for line in lines:
        line = str(line).strip('\n')
        if simplematch.match(pattern, line):
            matches.append(line)

    return matches


def main():
    print('***** Word Search *****')

    fileToSearchIn = input('Enter the name of the words file:\n')
    contents = getFileContents(fileToSearchIn)
    if(contents == None):
        print(f"Sorry, could not find file '{fileToSearchIn}'.")
        exit(code=1)

    patternToSearch = input("Enter a search pattern:\n")
    matches = getMatches(patternToSearch, getReadablePortion(contents))
    if len(matches) == 0:
        print(f"Sorry, matches for '{patternToSearch}' could not be found.")
    else:
        print(matches)


if __name__ == '__main__':
    main()
