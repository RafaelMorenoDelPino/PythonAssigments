# Assignment: Inter Planetary Weights

# Define surface gravity factor for each planet as constants
MERCURY_GRAVITY_FACTOR = 0.38
VENUS_GRAVITY_FACTOR = 0.91
MOON_GRAVITY_FACTOR = 0.165
MARS_GRAVITY_FACTOR = 0.38
JUPITER_GRAVITY_FACTOR = 2.34
SATURN_GRAVITY_FACTOR = 0.93
URANUS_GRAVITY_FACTOR = 0.92
NEPTUNE_GRAVITY_FACTOR = 1.12
PLUTO_GRAVITY_FACTOR = 0.066

# Get name and weight
sName = input("What is your name: ")
nWeight = float(input("What is your weight: "))

# Show formatted results for each planet
print(sName, "here are your weights on our Solar System's planets:") # No need to escape the single quote
print("{:20}".format("Weight on Mercury:"), format(MERCURY_GRAVITY_FACTOR * nWeight, "10.2f"))
print("{:20}".format("Weight on Venus:"), format(VENUS_GRAVITY_FACTOR * nWeight, "10.2f"))
print("{:20}".format("Weight on our Moon:"), format(MOON_GRAVITY_FACTOR * nWeight, "10.2f"))
print("{:20}".format("Weight on Mars:"), format(MARS_GRAVITY_FACTOR * nWeight, "10.2f"))
print("{:20}".format("Weight on Jupiter:"), format(JUPITER_GRAVITY_FACTOR * nWeight, "10.2f"))
print("{:20}".format("Weight on Saturn:"), format(SATURN_GRAVITY_FACTOR * nWeight, "10.2f"))
print("{:20}".format("Weight on Uranus:"), format(URANUS_GRAVITY_FACTOR * nWeight, "10.2f"))
print("{:20}".format("Weight on Neptune:"), format(NEPTUNE_GRAVITY_FACTOR * nWeight, "10.2f"))
print("{:20}".format("Weight on Pluto:"), format(PLUTO_GRAVITY_FACTOR * nWeight, "10.2f"))

