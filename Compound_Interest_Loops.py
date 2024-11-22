# Assignment: Compound Interest with Loops

# Initialize variables
fPrincipalInvestment = 0
fAnnualInterestRate = 0
iNumberOfMonths = 0
fGoalAmount = -1
iMonthsToAchieveGoal = 0

# For each input the user enters we check that it is valid and show message otherwise
while fPrincipalInvestment <= 0:
    try:
        fPrincipalInvestment = float(input("What is the Original Deposit (positive value): "))
        if fPrincipalInvestment <= 0:
            print("Input must be a positive numeric value")
    except ValueError:
        print("Input must be a positive numeric value")

while fAnnualInterestRate <= 0:
    try:
        fAnnualInterestRate = float(input("What is the Interest Rate (positive value)): "))
        if fAnnualInterestRate <= 0:
            print("Input must be a positive numeric value")
    except ValueError:
        print("Input must be a positive numeric value")

while iNumberOfMonths <= 0:
    try:
        iNumberOfMonths = int(input("What is the Number of Months (positive value)): "))
        if iNumberOfMonths <= 0:
            print("Input must be a positive numeric value")
    except ValueError:
        print("Input must be a positive numeric value")

while fGoalAmount < 0:
    try:
        fGoalAmount = int(input("What is the Goal Amount (can enter 0 but not negative)): "))
        if fGoalAmount < 0:
            print("Input must be 0 or greater")
    except ValueError:
        print("Input must be 0 or greater")

# Calculate monthly interest rate and set account balance to initial deposit for calculations
fMonthlyInterestRate = (fAnnualInterestRate / 100) / 12
fAccountBalance = fPrincipalInvestment

# Show the account balance for each month until it reaches the month we want
for iMonthCount in range(1, iNumberOfMonths + 1):
    fMonthlyInterest = fAccountBalance * fMonthlyInterestRate
    fAccountBalance += fMonthlyInterest
    print(f"Month: {iMonthCount} Account Balance is: $ {fAccountBalance:,.2f}")

# Set account balance to initial deposit for calculations
fAccountBalance = fPrincipalInvestment

# Calculate how many months it would take to achieve the desired goal amount
while fAccountBalance <= fGoalAmount:
    fMonthlyInterest = fAccountBalance * fMonthlyInterestRate
    fAccountBalance += fMonthlyInterest
    iMonthsToAchieveGoal += 1

# Show how many months it woult take to reach the goal
print(f"It will take: {iMonthsToAchieveGoal} months to reach the goal of $ {fGoalAmount:,.2f}")
