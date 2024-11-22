# Assignment: Grade Analyzer

# Number of tests the program will ask for
NUMBER_OF_TESTS = 4

# Initialize iTestsGradeTotal
iTestsGradeTotal = 0

# Get student's name
sStudentName = input("Name of the person we are calculating the grades for: ")

# Loop to calculate the tests total and the lowest grade
for iCount in range(NUMBER_OF_TESTS):
  iTestGrade = int(input(f"Test {iCount + 1}: "))

  # If the test grade if lower than 0, show message and stop program
  if iTestGrade < 0:
      print("Test Scores must be greater than 0")
      raise SystemExit

  # Set iLowestGrade with the first grade and update it after if the new grade is lower
  if iCount == 0 or iTestGrade < iLowestGrade: 
    iLowestGrade = iTestGrade

  iTestsGradeTotal += iTestGrade

# Ask to drop the lowest grade 
sDropLowestGrade = input(f"Do you wish to Drop the Lowest Grade Y or N?: ")

# Stop the program if the answer is not Y or N
if sDropLowestGrade != "Y" and sDropLowestGrade != "N":
  print("Enter a Y or N to Drop the Lowest Grade")
  raise SystemExit

# Do the test average calculation
if sDropLowestGrade == "Y": 
  iTestsAverage = (iTestsGradeTotal - iLowestGrade) / (NUMBER_OF_TESTS - 1)
else:
  iTestsAverage = iTestsGradeTotal / NUMBER_OF_TESTS

# Calculate Letter Grade
if iTestsAverage >= 97.0:
    sLetterGrade = 'A+'
elif iTestsAverage >= 94.0:
    sLetterGrade = 'A'
elif iTestsAverage >= 90.0:
    sLetterGrade = 'A-'
elif iTestsAverage >= 87.0:
    sLetterGrade = 'B+'
elif iTestsAverage >= 84.0:
    sLetterGrade = 'B'
elif iTestsAverage >= 80.0:
    sLetterGrade = 'B-'
elif iTestsAverage >= 77.0:
    sLetterGrade = 'C+'
elif iTestsAverage >= 74.0:
    sLetterGrade = 'C'
elif iTestsAverage >= 70.0:
    sLetterGrade = 'C-'
elif iTestsAverage >= 67.0:
    sLetterGrade = 'D+'
elif iTestsAverage >= 64.0:
    sLetterGrade = 'D'
elif iTestsAverage >= 60.0:
    sLetterGrade = 'D-'
else:
    sLetterGrade = 'F'

# Output results
print(f"{sStudentName} test average is: {iTestsAverage:.1f}")
print(f"Letter Grade for the test is: {sLetterGrade}")
