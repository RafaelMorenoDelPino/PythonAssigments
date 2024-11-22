# Assignment: Paint Job with Functions and Files
import math

# Gets and validates user input with the given prompt
def getFloatInput(prompt):
    fValue = -1
    while fValue <= 0:
        try:
            fValue = float(input(prompt))
            if fValue <= 0:
                print("Input must be a positive numeric value")
        except ValueError:
            print("Input must be a positive numeric value")

    return fValue

# Calculates Gallons of Paint rounded up
def getGallonsOfPaint(fWallSquareFeet, fFeetPerGallon):
    return math.ceil(fWallSquareFeet / fFeetPerGallon)

# Calculates Labour Hours
def getLaborHours(fLaborHoursPerGallon, iGallonsOfPaint):
    return fLaborHoursPerGallon * iGallonsOfPaint

# Calculates Labor Cost
def getLaborCost(fLabourHoursPerGallon, fLaborChargePerHour):
    return fLabourHoursPerGallon * fLaborChargePerHour

# Calculates Paint Cost
def getPaintCost(iGallonsOfPaint, fPaintPricePerGallon):
    return iGallonsOfPaint * fPaintPricePerGallon

# Returns Sales Tax by the given state code
def getSalesTax(sState):
    if sState == "CT" or sState == "VT":
        return 0.06
    elif sState == "MA":
        return 0.0625
    elif sState == "ME":
        return 0.085
    elif sState == "RI":
        return 0.07
    else:
        return  0

# Outputs data to console and text file
def showCostEstimate(iGallonsOfPaint, iLaborHours, fPaintCost, fLaborCost, fTax, sLastName):
    fTotalCost = fPaintCost + fLaborCost + fTax

    # Output calculations to console
    print(f"Gallons of paint: {iGallonsOfPaint}")
    print(f"Hours of labor: {iLaborHours}")
    print(f"Paint charges: ${fPaintCost:,.2f}")
    print(f"Labor charges: ${fLaborCost:,.2f}")
    print(f"Tax: ${fTax:,.2f}")
    print(f"Total cost: ${fTotalCost:,.2f}")

    # Create text file
    sFileName = f"{sLastName}_PaintJobOutput.txt"
    file = open(sFileName, "w")

    # Write data to file
    file.write(f"Gallons of paint: {iGallonsOfPaint}\n")
    file.write(f"Hours of labor: {iLaborHours}\n")
    file.write(f"Paint charges: ${fPaintCost:,.2f}\n")
    file.write(f"Labor charges: ${fLaborCost:,.2f}\n")
    file.write(f"Tax: ${fTax:,.2f}\n")
    file.write(f"Total cost: ${fTotalCost:,.2f}\n")

    # Close file after we are done with it
    file.close()

    print(f"File: {sFileName} was created.")

def main():
    # Get input data
    fWallSquareFeet = getFloatInput("Enter wall space in square feet: ")
    fPaintPricePerGallon = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGallon = getFloatInput("Enter feet per gallon: ")
    fLaborHoursPerGallon = getFloatInput("How many labor hours per gallon: ")
    fLaborChargePerHour = getFloatInput("Labor charge per hour: ")
    sState = input("State job is in: ").upper()
    sLastName = input("Customer Last Name: ")

    # Make calcualtions
    iGallonsOfPaint = getGallonsOfPaint(fWallSquareFeet, fFeetPerGallon)
    iLaborHours = getLaborHours(fLaborHoursPerGallon, iGallonsOfPaint)
    fPaintCost = getPaintCost(iGallonsOfPaint, fPaintPricePerGallon)
    fLaborCost = getLaborCost(iLaborHours, fLaborChargePerHour)
    fTax = getSalesTax(sState) * (fPaintCost + fLaborCost)

    # Show costs and write them to file
    showCostEstimate(iGallonsOfPaint, iLaborHours, fPaintCost, fLaborCost, fTax, sLastName)

main()
