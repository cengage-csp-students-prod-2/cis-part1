def caesar_decrypt(encrypted_text, distance):
    decrypted_text = ""
    
    for char in encrypted_text:
        # Check if the character is printable
        if char.isprintable():
            # Shift the character by the distance value
            # Wrap around using modulo for printable characters
            new_char = chr((ord(char) - 32 - distance) % 95 + 32)
            decrypted_text += new_char
        else:
            # If it's not printable, just append it as is
            decrypted_text += char
            
    return decrypted_text

def main():
    # Input encrypted text
    encrypted_text = input("Enter the encrypted text: ")
    
    # Input distance value
    while True:
        try:
            distance = int(input("Enter the distance value (shift): "))
            break
        except ValueError:
            print("Please enter a valid integer for the distance value.")
    
    # Decrypt the text
    decrypted_text = caesar_decrypt(encrypted_text, distance)
    
    # Output the decrypted plaintext
    print("Decrypted plaintext:", decrypted_text)

if __name__ == "__main__":
    main()