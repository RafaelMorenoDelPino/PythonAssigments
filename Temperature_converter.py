# Assignment: Temperature Converter

print("Rafael's Temp Converter:", end="\n\n")

# Get temperature and scale
fTemperature = float(input("Enter a temperature: "))
sTemperatureScale = input("Is the temp F for Fahrenheit or C for Celsius?: ").upper() # Making the input upper case here makes the rest of the code easier

# End program if the scale is not C or F
if sTemperatureScale != "C" and sTemperatureScale != "F":
    print("You must enter an F or C")
    raise SystemExit

# Print temperature equivalent if the input temp is not too high. Otherwise show error message.
if sTemperatureScale == "C": 
    if fTemperature > 100:
        print("Temp can not be > 100")
    else:
        fFahrenheitEquivalent = (9 / 5) * (fTemperature) + 32
        print(f"The Fahrenheit equivalent is: {fFahrenheitEquivalent:.1f}")
else: # The only possible value at this point is F, so we just need an else
    if fTemperature > 212:
        print("Temp can not be > 212")
    else:
        fCelsiusEquivalent = (5 / 9) * (fTemperature - 32)
        print(f"The Celsius equivalent is: {fCelsiusEquivalent:.1f}")
