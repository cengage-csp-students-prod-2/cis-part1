def shift_left(string):
    if len(string) == 0:
        return string  # Return empty string if input is empty
    # Shift left: move the first character to the end
    shifted_string = string[1:] + string[0]
    return shifted_string

def main():
    user_input = input("Enter a string: ")
    result = shift_left(user_input)
    
    print(f"Result after shifting left: {result}")

if __name__ == "__main__":
    main()