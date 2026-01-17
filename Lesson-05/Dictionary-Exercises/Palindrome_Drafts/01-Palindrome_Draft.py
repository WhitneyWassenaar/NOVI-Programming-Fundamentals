# Exercise: Write a program that checks whether a word is a palindrome.
# Bonus 1: Make it case-insensitive
# Bonus 2: Try to do th same with a sentence

# ---Exercise---
# BUG: Does not handle case differences or punctuation
word = input("Enter a word: ")

list_word = list(word)
list_word_reverse = list_word[::-1] # [::-1] Creates a new reversed list without modifying the original.

if list_word == list_word_reverse:
    print('Palindrome')
else:
    print('Not palindrome')

# When you use [::-1]
# The empty start and stop (:) mean "use the whole list"
# The '-1 step' moves through the list in reverse order
# Source: https://www.datacamp.com/tutorial/python-reverse-list

# ---Bonus 1---
# BUG: It works for single words, is case-insensitive but does not work with punctuations in sentences
word = input("Enter a word: ").lower()

list_word = list(word)
list_word_reverse = list_word[::-1] # [::-1] Creates a new reversed list without modifying the original.

if list_word == list_word_reverse:
    print('Palindrome')
else:
    print('Not palindrome')

# ---Bonus 2---
#BUG:
# Does not work because it compares the original string, including spaces, punctuation,
# and any non-letter characters, to its reversed version,
# so sentences or words with spaces or punctuation will not match even if they are palindromes.
# Example: "No lemon, no melon"

word = input("Enter a word: ").lower()

list_word = list(word)
list_word_reverse = list_word[::-1] # [::-1] Creates a new reversed list without modifying the original.

if list_word == list_word_reverse:
    print('Palindrome')
else:
    print('Not palindrome')

