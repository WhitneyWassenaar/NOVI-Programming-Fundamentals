# Caesar Cipher Encryptie/Decryptie

#Introduction

#The Caesar Cipher is a simple form of substitution encryption in which each letter in the text is replaced by a letter a fixed number of positions later in the alphabet. This application provides an easy way to encrypt or decrypt text using the Caesar Cipher.
#Julius Caesar himself used this method of encryption when sending important messages.
#The biggest drawback of this cipher is that there are only 25 possibilities, so a computer program can solve it quite easily.

#Instructions

#Enter the desired action: encode (encrypt) or decode (decrypt).
#Enter the text you want to encrypt or decrypt
#Specify the number of positions to shift the letters (shift number).
#The program will then display the encrypted or decrypted text, depending on the chosen action.

# decode: negative (left)
# encode: positive  (right)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def caesar_cipher(input_direction, input_text, input_shift):
    original_shift = input_shift
    new_text = ""

    if input_direction == "decode":
        input_shift *= -1

    for character in input_text:                                        # for each character in input text
        if character in alphabet:                                       # if character is also in alphabet
            character_index = alphabet.index(character)                 # the character index is the index of the character in alphabet
            new_character_index = (character_index + input_shift) % 26  # the new index is de index-number of the character + input shift
            new_text += alphabet[new_character_index]                   # to create the new text, add character on the new index of alphabet

        else:
            new_text += character # if the character from the text is not in alphabet, add the character unchanged

    print(f'You choose: {input_direction}, entered the text: {input_text}, with a shift of {original_shift}, you get {new_text}')

while True:
    direction = input("Enter 'decode' or 'encode': ").lower()
    text = input("Enter text: ")
    shift = int(input("Enter shift number: "))

    caesar_cipher(direction, text, shift)

    ask = input("Try again? (y/n): ")
    if ask == "n":
        break

