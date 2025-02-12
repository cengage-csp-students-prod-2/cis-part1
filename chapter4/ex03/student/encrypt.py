def caesar_encrypt(plaintext, distance):
    encrypted_text = ""
    
    for char in plaintext:
        # Check if the character is printable
        if char.isprintable():
            # Shift the character by the distance value
            # Wrap around using modulo for printable characters
            new_char = chr((ord(char) - 32 + distance) % 95 + 32)
            encrypted_text += new_char
        else:
            # If it's not printable, just append it as is
            encrypted_text += char
            
    return encrypted_text

def main():
    # Input plaintext
    plaintext = input("Enter the plaintext: ")
    
    # Input distance value
    while True:
        try:
            distance = int(input("Enter the distance value (shift): "))
            break
        except ValueError:
            print("Please enter a valid integer for the distance value.")
    
    # Encrypt the text
    encrypted_text = caesar_encrypt(plaintext, distance)
    
    # Output the encrypted text
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()