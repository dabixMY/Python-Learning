print("\t\t\tTransaction code: ")
print("\t\t\tS - 5  %")
print("\t\t\tM - 7  %")
print("\t\t\tL - 10 %\n")

# \t is for one tab
# \n is for one empty next line

code = input("Please enter the transaction code (S,M,L):").upper().strip()
if code in ['S', 'M', 'L']:

    price = float(input("Please enter price: RM"))
    emp_id = abs(int(input("Please enter employee ID: ")))

    if code == 'S':
        rate = 0.05
    elif code == 'M':
        rate = 0.07
    else:
        rate = 0.10

    commission = rate * price

    print(f"Employee ID :   {emp_id:10d}")
    print(f"Retail price: RM{price:10.2f}")
    print(f"Commission  : RM{commission:10.2f}")

else:
    print("Invalid transaction code!")
