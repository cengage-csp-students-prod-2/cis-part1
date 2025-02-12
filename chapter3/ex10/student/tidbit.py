# Prompt the user to enter the purchase price
purchase_price = float(input("Enter the purchase price: "))

# Constants
fixed_monthly_payment = 10.00  # Fixed monthly payment
annual_interest_rate = 0.12    # Annual interest rate (12%)

# Initialize balance and month
balance = purchase_price
month = 1

# Display the table headers
print("\nMonth  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")
print("--------------------------------------------------------------------------")

while balance > 0:
    # Calculate interest for the current month
    interest = balance * annual_interest_rate / 12

    # Calculate principal payment
    principal = fixed_monthly_payment - interest

    # Adjust for the final payment if the balance is less than the fixed payment
    if balance < fixed_monthly_payment:
        fixed_monthly_payment = balance + interest
        principal = balance

    # Calculate ending balance
    ending_balance = balance - principal

    # Display the current month's values
    print(f"{month:2d}      {balance:14.2f}          {interest:14.2f}          {principal:14.2f}      {fixed_monthly_payment:14.2f}      {ending_balance:14.2f}")

    # Update balance and move to the next month
    balance = ending_balance
    month += 1
