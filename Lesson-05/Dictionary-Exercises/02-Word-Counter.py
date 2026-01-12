# Write a program that counts how many words are in a sentence
# Bonus: Give the user the ability to enter a sentence and count the words

# ---Word Counter---

# ---Word Counter v1---
sentence = "I want to become a web developer!"

sentence = sentence.split() # split() splits a string into a list where each word is a list item
count = 0
for word in sentence:
    count += 1

print(f'{count} woorden')

# ---Word Counter v2---
sentence_1 = "I want to become a web developer!"
sentence_1 = sentence_1.split()

print(f'{len(sentence_1)} woorden')

# ---Word Counter v3
# Wrong, it only counts unique words
sentence_2 = "I want to become a web developer!"
words = {}
sentence_2_s = sentence_2.split()

for item in sentence_2_s:
    words[item] = 1

print(sum(words.values()))

# ---Word Counter v4---
sentence_3 = "I want to become a web developer!"

words = {} # Create an empty dictionary to add words
counter = 0 # Counts how many words are in the sentence

for word in sentence_3.split(): # For every item in the list 'sentence_3'
    words[counter] = word # Add a counter and the word from the list
    counter += 1

print(len(words)) # Length of dictionary == amount of words

# ---Bonus---
user_input = input('Write a sentence: ').split()
print(f'{len(user_input)} words in your sentence')

# ---Solution---
# The Exercise is: Write a program that counts how many words are in a sentence.
# This solution counts how many times each word appears in the sentence. It does not match what was asked.

# Language: Dutch
zin = "dit is een testzin om te testen of dit programma werkt"
aantal_woorden = {}

woorden = zin.split()
for woord in woorden:
    if woord in aantal_woorden:
        aantal_woorden[woord] += 1
    else:
        aantal_woorden[woord] = 1

print(aantal_woorden)