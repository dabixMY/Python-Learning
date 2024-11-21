num_line = int(input("Lines: "))
print()

for line in range(1, num_line * 2, 2):
    for space in range(1, num_line * 2 - line, 2):
        print(" ", end="")
    for star in range(1, line + 1, 1):
        print("*", end="")

    print()
