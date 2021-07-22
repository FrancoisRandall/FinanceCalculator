import math

# Request user input
# 2 '\t' commands are used for the vairable 'bond' to keep the indentations the same as for 'investment'.
# The '.lower() function is used to convert all types of text entered by the user to lowercase so that is can be recognised by the 'if' function.

menu_option = str(input('''Choose either 'invetment' or 'bond' from the menu below to proceed:

investment \t - to calculate the amount of interest you'll earn on interest
bond \t\t - to calculate the amount you'll have to pay on a home loan

Selection: ''').lower())

# Investment variables
# Request user input to add value to the below variables depending on the user input from 'menu_option'

if menu_option == "investment":

    deposit_amount = float(input("Please enter the amount you wish to deposit for your investment: "))
    invest_interest_rate = float(input("Please enter your investment interest rate here. Kindly only enter the number (no '%' needed): "))
    invest_years = float(input("Please enter the amount of years you wish to invest for: "))
    interest = str(input("Please confirm your preferred investment type: (compound/simple)").lower())
    compound_amount = round(deposit_amount * math.pow((1 + (invest_interest_rate / 100)), invest_years), 2)
    simple_amount = round(deposit_amount * (1 + (invest_interest_rate / 100) * invest_years), 2)

# Print summary of user's output for them to view

    print (f'''
    ------------------------------------------------------
    Deposit ammount:\t\t R{deposit_amount}
    Interest rate:\t\t {invest_interest_rate}%
    Years:\t\t\t {invest_years}
    Investment type:\t\t {interest}
    ------------------------------------------------------
    ''')

# Add value to the variable 'interest' depending on the input from the user

    if interest == "compound":
        print(f"Your investment of R{deposit_amount} for {invest_years} years with an interest rate of {invest_interest_rate}% will be R{compound_amount}.")

    elif interest == "simple":
        print(f"Your investment of R{deposit_amount} for {invest_years} years with an interest rate of {invest_interest_rate}% will be R{simple_amount}.")

    else: print("You did not select and appropriate answer")

# Bond variables
# Request user input to add value to the below variables depending on the user input from 'menu_option'

elif menu_option == "bond":

    house_value = float(input("Please enter the value of the house here: "))
    bond_interest = float(input("Please enter your annual bond interest rate here. Kindly only enter the number (no '%' needed): "))
    bond_interest_perc = round((bond_interest / 100) / 12, 2)
    repay_bond = float(input("Please enter the number of months that you plan to repay your bond here: "))
    monthly_payment = round(((bond_interest_perc * house_value) / (1 - (1 + bond_interest_perc)**-repay_bond)),2)

# Print summary of user's output for them to view

    print(f'''
    ------------------------------------------------------
    House value:\t\t\t R{house_value}
    Annual bond interest rate:\t\t {bond_interest}%
    Monthly bond interest rate:\t\t {bond_interest_perc}%
    Months to repay bond:\t\t {repay_bond}
    ------------------------------------------------------
    ''')

    print (f"You will have to pay R{monthly_payment} monthly to pay your bond off in {repay_bond} months.")

else: print("You have not selected an appropriate option")
