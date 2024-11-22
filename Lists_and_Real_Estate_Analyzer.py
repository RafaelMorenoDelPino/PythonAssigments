# Assignment: Lists and Real Estate Analyzer

# Gets and validates user input with the given prompt
def getFloatInput(prompt):
    fValue = -1
    while fValue <= 0:
        try:
            fValue = float(input(prompt))
            if fValue <= 0:
                print("Input a number that is greater than 0.")
        except ValueError:
            print("Input a number that is greater than 0.")

    return fValue

# Calculates the median value of a list
def getMedian(fSalesValues):
    iValuesLength = len(fSalesValues)

    # If the number of items in the list is odd, get the middle one
    iMedianIndex = iValuesLength // 2
    if iValuesLength % 2 == 1:
        return fSalesValues[iMedianIndex]
    else: # If the number of items is even get the middle one and the previous one, add them and divide by 2
        return (fSalesValues[iMedianIndex] + fSalesValues[(iMedianIndex) - 1]) / 2

def main():
    # Initialize variables
    fSalesValues = []
    sEnterMoreValues = "Y"

    # Append entered values to the fSalesValues list
    while sEnterMoreValues == "Y":
        fSalesValues.append(getFloatInput("Enter property sales value: "))
        sEnterMoreValues = input("Enter another value Y or N: ").upper()

        # If the answer is not Y or N, keep asking
        while sEnterMoreValues not in ["Y", "N"]:
            sEnterMoreValues = input("Enter another value Y or N: ").upper()

    fSalesValues.sort()

    # Output entered property values
    for iIndex in range(len(fSalesValues)):
        print(f"Property {iIndex + 1} $ {fSalesValues[iIndex]:15,.2f}")

    fTotalValue = sum(fSalesValues) # Calculate total here so we only do it once

    # Print the rest of values at the same time we do the calculations
    print(f"{'Minimum:':10} $ {min(fSalesValues):15,.2f}")
    print(f"{'Maximum:':10} $ {max(fSalesValues):15,.2f}")
    print(f"{'Total:':10} $ {fTotalValue:15,.2f}")
    print(f"{'Average:':10} $ {fTotalValue / len(fSalesValues):15,.2f}")
    print(f"{'Median:':10} $ {getMedian(fSalesValues):15,.2f}")
    print(f"{'Comission:':10} $ {fTotalValue * 0.03:15,.2f}")


main()
