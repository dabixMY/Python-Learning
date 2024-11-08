def prac4Q2a():
    actScore = int(input("Enter ACT score               >> "))
    topHalf = input("Enter topHalf (Y, Yes, N, No) >> ").upper()
    gpa = float(input("Enter gpa                     >> "))
    # ascertain if your values need to be explicitly converted

    # one-way
    cnt = 0  # cnt >= 2 eligible
    if actScore >= 18:
        cnt += 1
    # if topHalf == "Y" or "Yes" cannot do like this
    # if topHalf == "Y" or topHalf == "Yes": too long, not efficient
    if topHalf in ["Y", "Yes"]:
        cnt += 1
    if gpa >= 2.0:
        print("Eligible")
    else:
        print("Not eligible")

def prac4Q2b():
    actScore = int(input("Enter ACT score               >> "))
    topHalf = input("Enter topHalf (Y, Yes, N, No) >> ").upper()
    gpa = float(input("Enter gpa                     >> "))
    # ascertain if your values need to be explicitly converted

    # one-way
    cnt = 0  # cnt >= 2 eligible
    if actScore >= 18:
        cnt += 1
    # if topHalf == "Y" or "Yes" cannot do like this
    # if topHalf == "Y" or topHalf == "Yes": too long, not efficient
    if topHalf in ["Y", "Yes"]:
        cnt += 1
    if gpa >= 2.0:
        print("Eligible")
    else:
        print("Not eligible")

    actScore = int(input("Enter ACT score               >> "))
    topHalf = input("Enter topHalf (Y, Yes, N, No) >> ").upper()
    gpa = float(input("Enter gpa                     >> "))
    # ascertain if your values need to be explicitly converted

    # multi-way
    if actScore >= 18 and topHalf in ["Y", "Yes"] or actScore >= 18 and gpa >= 2.0:
        print("Eligible")
    else:
        print("Not eligible")


def prac4Q2c():
    eliList = ["Not eligible", "Eligible"]
    actScore = int(input("Enter ACT score               >> "))
    topHalf = input("Enter topHalf (Y, Yes, N, No) >> ").upper()
    gpa = float(input("Enter gpa                     >> "))

    idx = (actScore >= 18 and topHalf in ["Y", "Yes"] or \
           actScore >= 18 and gpa >= 2.0 or \
           topHalf in ["Y", "Yes"] and gpa >= 2.0) * 1
    print("%s" % eliList[idx])


def prac4Q2d():
    eliList = ["Not eligible", "Eligible"]
    actScore = int(input("Enter ACT score               >> "))
    topHalf = input("Enter topHalf (Y, Yes, N, No) >> ").upper()
    gpa = float(input("Enter gpa                     >> "))
    idx = (actScore >= 18 and topHalf in ["Y", "Yes"] or actScore >= 18 and gpa >= 2.0 or topHalf in ["Y", "Yes"] and gpa >= 2.0) * 1

    print(idx)
    print("%s" % eliList[idx])


def prac4Q2e():
    idx = 0
    actScore = int(input("Enter ACT score               >> "))
    topHalf = input("Enter topHalf (Y, Yes, N, No) >> ").upper()
    gpa = float(input("Enter gpa                     >> "))
    for topHalf in ["Y", "Yes"] or gpa >= 2.0 or actScore >= 18:
        idx = idx + 1
    if idx >= 2:
        print("Eligible")
    else:
        print("Not Eligible")
    print(idx)

# Uncomment to run
# prac4Q2a()
# prac4Q2b()
# prac4Q2c()
# prac4Q2d()
# prac4Q2e()
