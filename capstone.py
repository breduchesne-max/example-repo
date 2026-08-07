# Create a new Python file in the task folder called finance_calculators.py.
# At the top of the file include the line: import math
# Write the code that will do the following:
# The user should be allowed to choose which calculation they want to do.
# The first output that the user sees when the program runs should look like this:
# Investment - to calculate the amount of interest you'll earn on your investment.
# Bond - to calculate the amount you'll have to pay on a home loan.
# Enter either "investment" or "bond" from the menu above to proceed :

import math

print("Investment - to calculate the amount of interest you'll earn on your investment. \nBond - to calculate the amount you'll have to pay on a home loan. \nEnter either 'investment' or 'bond' from the menu above to proceed : ")


choice = input("Choose either 'Investment' or 'Bond' : ").strip().lower()

# 2. Direct the logic based on the choice
if choice == "Bond":
    print("You selected Bond.")

elif choice == "Investment":
    print("You selected Investment. Please choose either simple or compound :")

principal = float(input("Enter the principal amount : "))
rate = float(input("Enter the annual interest rate (5 for 5%): ")) / 100
time = float(input("Enter the time in years: "))

choice = input("Calculate (S)imple or (C)ompound interest? ").strip().upper()

if choice == "S":
    interest = principal * rate * time
    total = principal + interest
    print(f"\nSimple Interest: ${interest:,.2f} | Total Balance: ${total:,.2f}")

elif choice == "C":
    n = int(input("Enter compounding periods per year (1 for annually, 12 for monthly, or 365 for daily): "))
    total = principal * (1 + (rate / n)) ** (n * time)
    interest = total - principal
    print(f"\nCompound Interest: ${interest:,.2f} | Total Balance: ${total:,.2f}")

else:
    print("Invalid choice. ")




# Then ask the user to input if they want "simple" or "compound" interest, and store this in a variable called interest. 


# Depending on whether or not they typed "simple" or "compound", output the appropriate amount that they will get back after the given period at the specified interest rate. 
# Interest formulae:
# The total amount when simple interest is applied is calculated as follows: A = P(1 + r× t)
# The Python equivalent is very similar: A = P * (1 + p*t)
# The total amount when compound interest is applied is calculated as follows: A = P(1 + r)"
# The Python equivalent is slightly different: A = P * math.pow((1+r),t)
# In the formulae above:
# "'" is the interest entered above divided by 100, e.g., if 8% is entered, then "r" is 0.08.
# "P" is the amount that the user deposits.
# "'" is the number of years that the money is being invested.
# "A" is the total amount once the interest has been applied.