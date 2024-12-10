def validDate(date):

    mDays = [0, 31, 28, 31, 30, 31, 31, 31, 30, 31, 30, 31]
    status = True
    if not len(date) == 8 or not date.isdigit():
        status = False
    else:
        yyyy = int(date[:4])
        mm = int(date[4:6])
        dd = int(date[-2:])
        if yyyy%400 == 0:
            mDays[2] = 29
        #range
        if not (0 < mm <= 12) or not (0 < dd <= mDays[mm]):
            status = False

    return status


loop = True
step = 1 # use this if you have more than 1 input & validate
while loop:
    if step == 1:
        studID = input("Enter student ID >> ")
        if studID == "Q":
            loop = False
        elif not len(studID) == 10:
            print("Error, wrong student ID enter")
        else:
            step += 1

    if step ==2:
        date = input("Date yyyymmdd <Q>uit >> ")
        if date == "Q":
            loop = False
        elif not validDate(date):
            print("Error, invalid date entered")
        else:
            step += 1

