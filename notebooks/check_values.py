
"""
This program asks a user for 2 integer values, checks 
if the values are in the required range and prints the
result of adding and multiplying these values.
"""

print()

value1 = input("Enter an integer (between 1 and 99) value 1: ")
value1 = int(value1)

value2 = input("Enter an integer (between 1 and 99) value 2: ")
value2 = int(value2)

if (1 <= value1 <= 99) and (1 <= value2 <= 99):
    # Numbers are correct
    print(f"Two values multipled = {value1 * value2}")
    print(f"Two values summed = {value1 + value2}")

else:
    print("Both numbers must be between 1 and 99")
    
