age = abs(int(input("Please enter your age: "))) #abs() can get the absolute number such as -1 as 1

if age > 55:
    print("RM7")
elif 13 <= age <= 55:
    print("RM10")
elif 3 <= age <= 12:
    print("RM5")
else:
    print("Free")


