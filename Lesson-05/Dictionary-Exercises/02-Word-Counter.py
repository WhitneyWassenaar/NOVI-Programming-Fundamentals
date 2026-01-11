# Write a program that counts how many words are in a sentence
# Bonus: Give the user the ability to enter a sentence and count the words

# ---Word Counter---

# ---Word Counter v1---
sentence = "I want to become a web developer!"

sentence = sentence.split()                        # split() splits a string into a list where each word is a list item
count = 0
for word in sentence:
    count += 1

print(f'{count} woorden')

# ---Word Counter v2---
sentence = "I want to become a web developer!"
sentence = sentence.split()

print(f'{len(sentence)} woorden')

# ---Bonus---
user_input = input('Write a sentence: ').split()
print(f'{len(user_input)} words in your sentence')

# ---Solution---
# The Exercise is: Write a program that counts how many words are in a sentence. This solution counts how many times each word appears in the sentence. It does not match what was asked.
zin = "dit is een testzin om te testen of dit programma werkt"
aantal_woorden = {}

woorden = zin.split()
for woord in woorden:
    if woord in aantal_woorden:
        aantal_woorden[woord] += 1
    else:
        aantal_woorden[woord] = 1

print(aantal_woorden)