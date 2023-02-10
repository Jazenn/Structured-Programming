import string


def caesar_cijfer():
    input_tekst = input("Geef een tekst:")
    input_rotatie = int(input("Geef een rotatie:"))
    encrypted_text = str()

    if input_rotatie > 0:
        for letter in input_tekst:
            if letter in string.punctuation or letter == ' ':
                encrypted_text += letter
            else:
                ASCII_value = ord(letter) + input_rotatie
                encrypted_text += chr(ASCII_value)
        return encrypted_text

    elif input_rotatie < 0:
        for letter in input_tekst:
            if letter in string.punctuation or letter == ' ':
                encrypted_text += letter
            else:
                ASCII_value = ord(letter) - input_rotatie
                encrypted_text += chr(ASCII_value)
        return encrypted_text

    else:
        return input_tekst


print(caesar_cijfer())