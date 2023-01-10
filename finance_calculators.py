import math

# print introduction
print("Choose either 'investment' or 'bond' from the menu below to proceed: \n")
print("Investment  -  to calculate the amount of interest you'll earn on your investment")
print("Bond        -  to calculate the amount you'll have to pay on a home loan")

# get choice input, expecting either "invesment" or "bond"
choice = input("Enter 'investment' or 'bond': ").lower()

while choice != "investment" and choice != "bond":
    choice = input("Please try again: ").lower()

# Investment
if choice == "investment":

    # How much?
    while True:
        try:
            deposit_amount = float(input("How much money are you depositing? "))
            break
        except:
            print("Input type is not valid.")

    # % Rate?
    while True:
        try:
            interest_rate = float(input("What is the interest rate (%)? "))
            break
        except:
            print("Input type not valid.")

    # How many years?
    while True:
        try:
            duration = float(input("How many years do you plan to invest? "))
            break
        except:
            print("Input type not valid.")

    # What type of investment?
    print("What type of investment would you like to make?")
    invest_type = input("Simple or Compound? ").lower()
    while invest_type != "simple" and "compound":
        invest_type = input("Simple or Compound? ").lower()

    # Convert the % rate into the appropriate number that will allow the calculation to complete
    r = interest_rate / 100 

    # SIMPLE INTEREST:
    if invest_type == "simple": 
        # Formula for simple interest
        total = round(deposit_amount * (1 + r * duration), 2)
        print(f"£{total}")
    # COMPOUND INTEREST
    elif invest_type == "compound":
        # Formula for compound interest
        total = round(deposit_amount * math.pow((1 + r), duration), 2)
        print(f"£{total}")

# Bond
elif choice == "bond":
    # House Value
    while True:
        try:
            house_value = float(input("What is the current value of your house? "))
            break
        except:
            print("Input type not valid.")
    # Interest rate
    while True:
        try:
            interest_rate = float(input("What is the annual interest rate (%)? "))
            break
        except:
            print("Input type not valid.")
    # How many months to repay?
    while True:
        try:
            repay_duration = float(input("How many months do you expect to pay this back in? "))
            break
        except:
            print("Input type not valid.")

    # convert the % rate into the appropriate number that will allow the calculation to complete
    r = interest_rate / 100
    monthly_interest = r / 12

    # formula for bond repayment
    monthly_repayments = round((monthly_interest * house_value) / (1 - (1 + monthly_interest)**(-repay_duration)), 2)
    print(f"You will need to repay £{round(monthly_repayments / 12, 2)} each month!")