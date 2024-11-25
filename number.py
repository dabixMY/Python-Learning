def main():
    x = get_int("What's x? ")
    print(f"x is {x}.")

def get_int(prompt):
    while True:
        try:
            # ──> Shortest method: directly return the value.
            # ──> Downside: potential readability issues.
            return int(input(prompt))

            # ──> Original successful approach:
            # ──> x = int(input(prompt))
            # ──> return x

        except ValueError:
            # ──> Handle the case where input is not a valid integer.
            print("x is not an integer.")

            # ──> 'pass' can be used here to restart the loop, but:
            # ──> It may not clearly communicate to the user what went wrong.
            # ──> The user might be uncertain of what to input next.

        # ──> Alternative loop termination approach (commented out for clarity):
        # ──> else:
        # ──>     return x

main()
