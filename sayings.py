# ──> Define the main function to coordinate the script's execution.
def main():
    # ──> Call the 'hello' function with "world" as the argument.
    hello("world")
    # ──> Call the 'goodbye' function with "world" as the argument.
    goodbye("world")


# ──> Define a function to print a greeting message.
def hello(name):
    print(f"hello, {name}")


# ──> Define a function to print a farewell message.
def goodbye(name):
    print(f"goodbye, {name}")


# ──> Ensure the script runs directly, not when imported as a module.
# ──> This block prevents unintended execution when imported elsewhere.
if __name__ == "__main__":
    main()
