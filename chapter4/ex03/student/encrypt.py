def caesar_encrypt(plaintext, distance):
    encrypted_text = ""
    
    for char in plaintext:
        if char.isprintable():
            new_char = chr((ord(char) - 32 + distance) % 95 + 32)
            encrypted_text += new_char
        else:
            encrypted_text += char
            
    return encrypted_text

def encrypt_file(input_file, output_file, distance):
    with open(input_file, 'r', encoding='utf-8') as infile:
        plaintext = infile.read()
    
    encrypted_text = caesar_encrypt(plaintext, distance)
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(encrypted_text)

def main():
    input_file = input("Enter the input file name (to encrypt): ")
    output_file = input("Enter the output file name (for encrypted text): ")
    
    while True:
        try:
            distance = int(input("Enter the distance value (shift): "))
            break
        except ValueError:
            print("Please enter a valid integer for the distance value.")
    
    encrypt_file(input_file, output_file, distance)
    print(f"File '{input_file}' has been encrypted and saved as '{output_file}'.")

if __name__ == "__main__":
    main()