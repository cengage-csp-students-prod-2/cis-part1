# encrypt.py

def caesar_cipher(plaintext, distance):
    encrypted_text = []
    
    for char in plaintext:
        # Shift only printable ASCII characters
        if 32 <= ord(char) <= 126:
            # Calculate the new character with wrapping
            shifted_char = chr((ord(char) - 32 + distance) % 95 + 32)
            encrypted_text.append(shifted_char)
        else:
            encrypted_text.append(char)  # Keep non-printable characters unchanged
    
    return ''.join(encrypted_text)

def main():
    plaintext = input("Enter the plaintext: ")
    
    while True:
        try:
            distance = float(input("Enter the distance value (integer): "))
            break
        except ValueError:
            print("Please enter a valid integer for the distance value.")
    
    encrypted_text = caesar_cipher(plaintext, distance)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()