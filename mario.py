def main():
    print_column(4)


def print_column(height):
    # Print a column of the specified height
    print("#\n" * height, end="")
    print_row(4)


def print_row(width):
    # Print a row of the specified width
    print("?" * width)
    print_square(3)


def print_square(size):
    # For each row in the square
    for i in range(size):
        # For each brick in the row (old method)
        # for j in range(size):
        #     # Print brick
        #     print("#", end="")
        # print()

        # Print an entire row of bricks (new method)
        print("#" * size)


main()
