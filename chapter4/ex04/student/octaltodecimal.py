def octal_to_decimal(octal_str):
    try:
        decimal_value = int(octal_str, 8)
        return decimal_value
    except ValueError:
        print("Invalid octal number.")
        return None

def main():
    octal_input = input("Enter an octal number: ")
    decimal_output = octal_to_decimal(octal_input)
    
    if decimal_output is not None:
        print(f"The decimal representation of octal {octal_input} is: {decimal_output}")

if __name__ == "__main__":
    main()