def shift_right(string):
    if len(string) == 0:
        return string  # Return empty string if input is empty
    # Shift right: move the last character to the front
    shifted_string = string[-1] + string[:-1]
    return shifted_string

def main():
    user_input = input("Enter a string: ")
    result = shift_right(user_input)
    
    print(f"Result after shifting right: {result}")

if __name__ == "__main__":
    main()
