# define strings
firstname = "Bugs"
lastname = "Bunny"

#define our sequence
sequence = (firstname,lastname)

#join into new string
name = " ".join(sequence)
print(name)

words = ["How","are","you","doing","?"]
sentence = ' '.join(words)
print(sentence)

"""
Exercise
Try the exercises below

1.Create a list of words and join them, like the example above.
2.Try changing the seperator string from a space to an underscore.
"""

#Create a list of words and join them, like the example above.
words = ["How","do","you","do","?"]
sentence = ' '.join(words)
print(sentence)

#Try changing the seperator string from a space to an underscore.
words = ["How", "do", "you", "do", "?"]
sentence = '_'.join(words)
print(sentence)
