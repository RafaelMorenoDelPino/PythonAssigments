# Assignment: Compound Interest

# Get necessary data for calculations. I am making the assumption that for the number of years the user will enter a whole number
fPrincipalInvestment= float(input("Enter the starting principal: "))
fAnnualInterestRate = float(input("Enter the annual interest rate: ")) / 100 # Interest rate is a percentage so it needs to be divided by 100 to convert it to decimal
iCompoundingTimesPerYear = int(input("How many times per year is the interest compounded?: "))
iYearsEarningInterest = int(input("For how many years will the account earn interest?: "))

# Calculate compound interest based on the entered data
fFutureValue = fPrincipalInvestment * (1 + fAnnualInterestRate / iCompoundingTimesPerYear) ** (iCompoundingTimesPerYear * iYearsEarningInterest)

# Output future value
print("At the end of", iYearsEarningInterest, "years you will have $", format(fFutureValue, ',.2f'))


