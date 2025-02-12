# encrypt.py

def caesar_cipher(plaintext, distance):
    encrypted_text = []
    
    for char in plaintext:
        # Check if the character is printable
        if 32 <= ord(char) <= 126:  # Only shift printable ASCII characters
            # Shift the character by the distance
            shifted_char = ord(char) + distance
            
            # Wrap around if it goes beyond printable characters
            if shifted_char > 126:
                shifted_char = 32 + (shifted_char - 127)  # Wrap around to start from 32
            
            encrypted_text.append(chr(shifted_char))
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