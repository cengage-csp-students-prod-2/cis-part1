def shift_left(bit_string):
    if len(bit_string) == 0:
        return bit_string  # Return empty string if input is empty
    # Shift left: move the first character to the end
    shifted_string = bit_string[1:] + bit_string[0]
    return shifted_string

def encrypt(input_string):
    encrypted_bits = []
    
    for char in input_string:
        # Add 1 to the ASCII value of the character
        ascii_value = ord(char) + 1
        
        # Convert the new ASCII value to a binary string
        bit_string = bin(ascii_value)[2:]  # Remove the '0b' prefix
        
        # Shift the bits to the left
        shifted_bits = shift_left(bit_string)
        
        # Append the shifted bits to the list
        encrypted_bits.append(shifted_bits)
    
    # Join the encrypted bit strings with a space
    encrypted_output = ' '.join(encrypted_bits)
    return encrypted_output

def main():
    input_string = input("Enter a string to encrypt: ")
    encrypted_output = encrypt(input_string)
    print(f"Encrypted output: {encrypted_output}")

if __name__ == "__main__":
    main()