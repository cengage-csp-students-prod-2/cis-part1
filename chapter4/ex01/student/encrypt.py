def caesar_cipher(text, distance):
    encrypted_text = ""
    for char in text:
        if char.isprintable():
            encrypted_char = chr((ord(char) + distance) % 256)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    plaintext = input("Enter the plaintext: ")
    distance = int(input("Enter the distance value: "))
    encrypted_text = caesar_cipher(plaintext, distance)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()