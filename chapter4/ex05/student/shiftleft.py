def shift_left(bit_string):
    if not all(bit in '01' for bit in bit_string):
        print("Invalid input: Please enter a valid bit string (only 0s and 1s).")
        return None
    
    # Shift left: move the leftmost bit to the rightmost position
    shifted_string = bit_string[1:] + bit_string[0]
    return shifted_string

def main():
    bit_string = input("Enter a bit string: ")
    result = shift_left(bit_string)
    
    if result is not None:
        print(f"Result after shifting left: {result}")

if __name__ == "__main__":
    main()
