# Exercise: Write a program that checks whether a word is a palindrome.
# Bonus 1: Make it case-insensitive
# Bonus 2: Try to do the same with a sentence

# ---Exercise V1---
dictionary_woorden = {}

invoer_woord = input('Voer een woord in: ').lower()

def palindrome(invoer_woord):                             # BUG: Parameter moet niet hetzelfde als input zijn
    invoer_woord_list = list(invoer_woord)                # Het converteren van string naar list is overbodig
    invoer_woord_list_reverse = invoer_woord_list[::-1]   # [::-1] zet niet alleen lijsten in omgekeerde volgorde maar ook strings!

    if invoer_woord_list == invoer_woord_list_reverse:
        return True                                       # Overbodig, als je een conditioneel statement schrijft dan geeft dat automatisch False/True terug
    else:
        return False

dictionary_woorden[invoer_woord] = palindrome(invoer_woord)

print(dictionary_woorden)

# ---Exercise V2---
# Enter 1 word and check if word is palindrome
# Only works for single words
enter_word = input("Enter word: ").lower()

dictionary_words = {}

def is_palindrome(word):
    return word == word[::-1]

dictionary_words[enter_word] = is_palindrome(enter_word)
print(dictionary_words)

# ---Exercise V3---
# Add multiple words and exit to check which words are palindromes

dictionary_words1 = {}
while True:

    enter_word1 = input("Enter word: ").lower()

    def is_palindrome(word):                                     # BUG: For iteration this function is defined every time the user enters input. This is unnecessary.
        return word == word[::-1]

    dictionary_words1[enter_word1] = is_palindrome(enter_word1)

    add_word = input("Add another word? (yes/no): ")
    if add_word == "no":                                         # BUG: Case-sensitive
        break
print(dictionary_words1)

# ---Bonus 1 and 2---
dictionary_of_words = {}

def palindrome_check(word):
    return word == word[::-1]

while True:
    user_input = input("Enter word: ").lower().replace(" ","") # This works for sentences or words with spaces.

    dictionary_of_words[user_input] = palindrome_check(user_input)

    add_another_word = input("Add another word?\n(yes/no): ")

    if add_another_word.lower() == "no":
        break

print(dictionary_of_words)