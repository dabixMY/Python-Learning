# ──> List Method: Using a list to store numbers for averaging.
from statistics import mean  # ──> Importing 'mean' for averaging.

# ──> Step 1: Create an empty list to store numbers.
num_list = []

# ──> Step 2: Get the total number of inputs from the user.
total_count = int(input("Total number to key in >> "))

# ──> Step 3: Populate the list with numbers entered by the user.
# ──> Initialisation, condition check, and adjustment within the loop.
for count in range(0, total_count, 1):
    number = float(input("Key in number >> "))
    num_list.append(number)

# ──> Step 4: Calculate the average using the list method.
# ──> Option 1 (commented out): Using 'sum' and 'len' functions.
# average = sum(num_list) / len(num_list)

# ──> Option 2: Using 'mean' for simplicity and clarity.
average = mean(num_list)

# ──> Step 5: Print the average, formatted to two decimal places.
print(f"Average : {average:.2f}")
