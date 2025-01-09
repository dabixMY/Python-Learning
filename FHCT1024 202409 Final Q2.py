with open("libtrans.txt", "r") as file:
    lines = file.readlines()
rec = [line.strip("\n").split("|") for line in lines]
date = input("Date (YYYYMMDD)    >> ")
id = input("Lecturer/Student ID>> ")
bookborrow = sum(1 for record in rec if record[0] == id)

print(f"Book(s) borrowed: {bookborrow}")

role = 'Lecturer' if len(id) == 5 else 'Student'

maxborrow = 10 if role == 'Lecturer' else 3
dayborrow = 30 if role == "Lecturer" else 7

bookid = None

while bookid != 'Q':
    bookid = input("Book ID <Q>uit     >> ")

    if bookid == 'Q':
        break

    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[-2:])
    daylst = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        daylst[2] = 29

    dueday = day + dayborrow
    duemonth = month
    dueyear = year
    if dueday > daylst[month]:
        dueday = dueday - daylst[month]
        duemonth += 1
    if duemonth > 12:
        duemonth = duemonth - 12
        dueyear += 1
    duedate = f"{dueyear}{duemonth:02}{dueday:02}"
    print(f"Due date            : {duedate}")

    with open("libtrans.txt", "a") as file:
        file.write("|".join([id, bookid, date, duedate]) + "\n")

    bookborrow += 1

    if bookborrow == maxborrow:
        print("Max number of borrowed books reached")
        break
