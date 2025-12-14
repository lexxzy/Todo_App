feet_Inches = input("Enter feet and inches separated by a space: ")
def feet_to_inches(feet_Inches):
    feet, inches = feet_Inches.split()
    feet = float(feet)
    inches = float(inches)
    total_inches = feet * 12 + inches
    return total_inches

print(feet_to_inches(feet_Inches))