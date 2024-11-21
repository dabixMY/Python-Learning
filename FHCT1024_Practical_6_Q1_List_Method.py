# List method

num_list = []

total_count = int(input("Total number to key in >> "))

                 # Initialisation, condition check, adjustment
for count in range(0, total_count, 1):
    number = float(input("Key in number >> "))
    num_list.append(number)

        # Add all values in the list
average = sum(num_list) / len(num_list)  # Count how many items in the list

print(f"Average : {average:.2f}")
