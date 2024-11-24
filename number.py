try:
    x = int(input("What's x? "))
    # print(f"x is {x}.")  # Original successful approach
except ValueError:
    # Handle the case where input is not a valid integer
    print("x is not an integer.")
else:
    # Execute if no exception occurs
    print(f"x is {x}.")
