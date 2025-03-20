# Method Cesar Cipher

def cipher_cesar(message):
    cipher = ''
    for char in message:
        if char.isalpha():
            char = char.upper()
            code = ord(char) + 1
            if code > ord('Z'):
                code = ord('A')
            cipher += chr(code)
        else:
            cipher += chr
    return cipher

print(cipher_cesar("JORMAN"))


def descipher_cesar(cipher):
    text = ''
    for char in cipher:
        if char.isalpha():
            char = char.upper()
            code = ord(char)- 1
            if code < ord('A'):
                code = ord('Z')
            text += chr(code)
        else:
            text += char
    return text

print(descipher_cesar("KPSNBO!"))
