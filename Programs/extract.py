# A programs that extracts data from an output of a sensor- Assignment 5.
# Batandwa Mgutsi
# 10/05/2020


def location(block):
    """Returns the location component in block in title case."""
    # The location component starts emidiately after the second space.
    sub = block[block.find('BEGIN')+6:block.find('END')-1]
    locationString = sub[sub.find(' ')+1:]

    # Make it lower case, reverse it, and make only the first letter  upper case.
    locationString = locationString.lower()[len(locationString)::-1]
    return locationString.title()


def temperature(block):
    """Returns the temperature componet in block as a real number value."""
    start = block.find('BEGIN')+6
    end = block.find('_')
    return float(block[start:end])


def x_coordinate(block):
    """Returns the x-coordinate component in block as a string."""
    start = block.find(':')+1
    end = block.find(',')
    return block[start:end]


def y_coordinate(block):
    """Returns the y-coordinate component in block as a string."""
    start = block.find(',')+1

    # Skip the first space
    end = block.find(' ', block.find(' ')+1)
    return block[start:end]


def pressure(block):
    """Returns the pressure component in block as a real number."""
    start = block.find('_')+1
    end = block.find(':')
    return float(block[start:end])


def get_block(data):
    """Extracts the sub string starting with 'BEGIN' and ending with 'END'"""
    start = data.find('BEGIN')
    end = data.find('END')+3
    return data[start:end]


def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))


if __name__ == '__main__':
    main()
