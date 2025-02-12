def shift_right(bit_string):
    if not all(bit in '01' for bit in bit_string):
        print("Invalid input: Please enter a valid bit string (only 0s and 1s).")
        return None
    
    # Shift right: move the rightmost bit to the leftmost position
    shifted_string = bit_string[-1] + bit_string[:-1]
    return shifted_string

def main():
    bit_string = input("Enter a bit string: ")
    result = shift_right(bit_string)
    
    if result is not None:
        print(f"Result after shifting right: {result}")

if __name__ == "__main__":
    main()
