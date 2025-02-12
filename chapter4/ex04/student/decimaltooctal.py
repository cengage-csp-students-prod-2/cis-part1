def decimal_to_octal(decimal_num):
    try:
        octal_value = oct(decimal_num)[2:]  # Remove the '0o' prefix
        return octal_value
    except ValueError:
        print("Invalid decimal number.")
        return None

def main():
    decimal_input = input("Enter a decimal number: ")
    
    try:
        decimal_num = int(decimal_input)
        octal_output = decimal_to_octal(decimal_num)
        
        if octal_output is not None:
            print(f"The octal representation of decimal {decimal_num} is: {octal_output}")
    except ValueError:
        print("Invalid decimal number.")

if __name__ == "__main__":
    main()
