# Non-list method

total = 0

total_count = int(input("Total number to key in >> "))

                 # Initialisation, condition check, adjustment
for count in range(0, total_count, 1):
    number = float(input("Key in number >> "))
    total += number

average = total / total_count

print(f"Average : {average:.2f}")
