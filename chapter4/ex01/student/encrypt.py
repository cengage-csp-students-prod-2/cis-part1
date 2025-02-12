def caesar_cipher(plaintext, distance):
    encrypted_text = []
    
    for char in plaintext:
        # Check if the character is printable
        if char.isprintable():
            # Shift the character by the distance
            shifted_char = chr((ord(char) + distance) % 256)
            encrypted_text.append(shifted_char)
        else:
            # If not printable, keep the character unchanged
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

def main():
    # Input plaintext from the user
    plaintext = input("Enter the plaintext: ")
    
    # Input distance value from the user
    while True:
        try:
            distance = int(input("Enter the distance value (integer): "))
            break
        except ValueError:
            print("Please enter a valid integer for the distance value.")
    
    # Encrypt the plaintext
    encrypted_text = caesar_cipher(plaintext, distance)
    
    # Output the encrypted text
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
