
# Extracts the an colour the colour of the fox in the string 'the quick brown fox jumps...'
# Batandwa Mgutsi
# 04/03/2020

sentence = 'The quick brown fox jumps over the lazy dog'

# The one is the size of the space before the colour
start = sentence.find('quick')+5+1

# The one is the size of the space after the colour
end = sentence.find('fox')-1

colour = sentence[start:end]
print(f"The original colour was '{colour}'")

# Now change the colour of the fox
newColour = 'green'
newSentence = sentence.replace(colour, newColour)
print(f"After changing the colour, the new sentence is '{newSentence}'")
