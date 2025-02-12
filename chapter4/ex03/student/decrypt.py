def caesar_decrypt(encrypted_text, distance):
    decrypted_text = ""
    
    for char in encrypted_text:
        if char.isprintable():
            new_char = chr((ord(char) - 32 - distance) % 95 + 32)
            decrypted_text += new_char
        else:
            decrypted_text += char
            
    return decrypted_text

def decrypt_file(input_file, output_file, distance):
    with open(input_file, 'r', encoding='utf-8') as infile:
        encrypted_text = infile.read()
    
    decrypted_text = caesar_decrypt(encrypted_text, distance)
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(decrypted_text)

def main():
    input_file = input("Enter the input file name (to decrypt): ")
    output_file = input("Enter the output file name (for decrypted text): ")
    
    while True:
        try:
            distance = int(input("Enter the distance value (shift): "))
            break
        except ValueError:
            print("Please enter a valid integer for the distance value.")
    
    decrypt_file(input_file, output_file, distance)
    print(f"File '{input_file}' has been decrypted and saved as '{output_file}'.")

if __name__ == "__main__":
    main()