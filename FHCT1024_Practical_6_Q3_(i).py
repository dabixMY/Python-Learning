# Output: Increasing triangle of stars (stars increase each line)
num_line = int(input("Lines: "))
print()

for line in range(1, num_line + 1, 1):
    for star in range(1, line + 1, 1):
        print("*", end="")

    print()

# Alternative method to print the increasing triangle
# num_line = int(input("Lines: "))
# print()
#
# for line in range(1, num_line + 1):
#     print('*' * line)  # Print 'line' number of asterisks on this line

# Output: Decreasing triangle of stars (stars decrease each line)
# num_line = int(input("Lines: "))
# print()
#
# for line in range(1, num_line + 1, 1):
#     for star in range(1, (num_line + 2) - line, 1): #arithmetic progression
#         print("*", end="")
#
#     print()
