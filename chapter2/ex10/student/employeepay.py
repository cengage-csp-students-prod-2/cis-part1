# Write your program here

hourly = float(input("Enter your hourly wage: "))
hours = float(input("Enter your total hours worked: "))
overtimehours = float(input("Enter your total overtime hours worked: "))


overtime = hourly * 1.5
regularpay= hours * hourly
totalpay= overtimehours + regularpay
print(f"Your total weekly pay is {totalpay}")