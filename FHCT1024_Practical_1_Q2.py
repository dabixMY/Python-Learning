"""
Sample Output:

Please key in the number of wheels: 4
Please key in the price: RM138888.88
Please key in the license type: D
Please key in the registration no.: AAA1234

This vehicle has 4 wheels. The price is RM138888.88.
You are to have a Type D driving license.
The registration no. of this vehicle is AAA1234.
"""

while True:
    try:
        wheels = int(input("Please key in the number of wheels: "))
        break # Exit loop if input is valid
    except ValueError:
        pass # Do nothing and just repeat the loop

while True:
    try:
        price = float(input("Please key in the price: RM"))
        break # Exit loop if input is valid
    except ValueError:
        pass # Do nothing and just repeat the loop


while True:
    licT = input("Please key in the license type: ").upper() # Convert input to uppercase
    validT = {'A', 'B', 'B1', 'B2', 'C', 'D', 'DA', 'E', 'F', 'G', 'H', 'I', 'M'}
    if licT in validT:
        pass
        break # Exit loop if input is valid
    else:
        print("Invalid license type! Please key in a valid license type.")

regNo = input("Please key in the registration no.: ").upper().strip() # Convert input to uppercase and remove whitespace

print()
print("This vehicle has", wheels, "wheels.", end=" ")
print("The price is RM{:.2f}".format(price)+".")
print("You are to have a Type", licT, "driving license.")
print("The registration no.of this vehicle is", regNo+".")