cont = "y"
print("        Coffee        |          Pastry")
print("Espresso   RM10.00    |  Croissant       RM2.00")
print("Cappuccino RM11.00    |  Muffin          RM3.00")
print("Latte      RM12.00    |  Scone           RM5.00")
print()

while cont == "y":
    print("Insert quantity of your order:")
    esp = int(input("Espresso  : "))
    cap = int(input("Cappuccino: "))
    lat = int(input("Latte     : "))
    cro = int(input("Croissant : "))
    muf = int(input("Muffin    : "))
    sco = int(input("Scone     : "))
    print()
    cont = input("Do you want to edit your order? [y/n]: ")

print("Here is your order summary:")
print(f"Espresso  : {esp} x RM10.00 = RM{esp * 10:.2f}")
print(f"Cappuccino: {cap} x RM11.00 = RM{cap * 11:.2f}")
print(f"Latte     : {lat} x RM12.00 = RM{lat * 12:.2f}")
print(f"Croissant : {cro} x RM 2.00 = RM{cro * 2:.2f}")
print(f"Muffin    : {muf} x RM 3.00 = RM{muf * 3:.2f}")
print(f"Scone     : {sco} x RM 5.00 = RM{sco * 5:.2f}")

total = esp * 10 + cap * 11 + lat * 12 + cro * 2 + muf * 3 + sco * 5
print(f"Total = RM{total:.2f}")
print()

point = total * 2
print(f"You have earned {point} loyalty points from this order.")
print("Thank you")
