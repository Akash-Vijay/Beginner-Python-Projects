"""

*   File                  :       02_tip_calculator.py
*   Description           :       Program to calculate the tip of a bill
*   Creator               :       Akash Vijay
*   Date                  :       December 5, 2021

"""

print("\nWelcome to the Tip Calculator\n")

bill = float(input("Enter the total bill amount: "))
people = float(input("Enter the number of people: "))
tip_percent = float(input("Enter the percent of tip: "))

tip = (bill + (bill * (tip_percent/100))) / people
print(f"Your share of the bill is {tip}")