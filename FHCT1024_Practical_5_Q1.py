repeat = True

while repeat:
    fahrenheit = float(input("Enter temperature (in F) >> "))

    if fahrenheit != 999:
        celsius = (fahrenheit - 32) * (5 / 9)
        print(f"Temperature: {celsius:.2f} C")
        print(f"{fahrenheit:.2f} F = {celsius:.2f} C")
    else:
        print("Thank you for using our program :D")
        repeat = False
