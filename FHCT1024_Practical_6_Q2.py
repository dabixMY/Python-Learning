start = int(input("Staring number >> "))
end = int(input("Ending  number >> "))
for num in range(start, end + 1, 1):
    print()  # Space then follow by table
    for count in range(1, 13, 1):
        print(f"{num:2d} x {count:2d} = {num * count:3d}")

    print()  # Table then follow by space
