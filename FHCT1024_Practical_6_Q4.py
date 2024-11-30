target = int(input("Enter an integer >> "))

for number in range(2, target + 1):
    zero_counter = 0

    for check in range(1, number + 1):
        if number % check == 0:
            zero_counter += 1

    if zero_counter == 2:
        print(f"{number}", end=" ")
