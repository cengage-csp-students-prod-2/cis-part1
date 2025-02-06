"""
File: tidbit.py
This program calculates and displays a payment schedule for a loan at TidBit Computer Store.
The user inputs the purchase price, and the program outputs a table with the payment schedule for the lifetime of the loan.
"""

# Prompt the user to enter the purchase price
purchase_price = float(input("Enter the purchase price: "))

# Constants
down_payment_rate = 0.10
annual_interest_rate = 0.12
monthly_payment_rate = 0.05

# Calculate the initial values
down_payment = purchase_price * down_payment_rate
balance = purchase_price - down_payment
monthly_payment = purchase_price * monthly_payment_rate

# Display the table headers
print("\nMonth  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")
print("--------------------------------------------------------------------------")

month = 1
while balance > 0:
    interest = balance * annual_interest_rate / 12
    principal = monthly_payment - interest
    if balance < monthly_payment:
        monthly_payment = balance + interest
        principal = balance
    ending_balance = balance - principal
    
    # Display the current month's values
    print(f"{month:2d}      {balance:12.2f}          {interest:12.2f}          {principal:12.2f}      {monthly_payment:12.2f}      {ending_balance:12.2f}")
    
    # Update the balance and month
    balance = ending_balance
    month += 1