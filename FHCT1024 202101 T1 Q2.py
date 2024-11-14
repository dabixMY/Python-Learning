# Collecting Student and Session Data
stuName = input("Student’s name -         >> ").strip().title()
stuID = input("Student’s ID            >> ").strip()
sesDate = input("Session’s Date          >> ").strip()
sesStime = input("Session’s Start Time    >> ")
sesEtime = input("Session’s End Time      >> ")
sesType = input("Session’s Type (L, P, T)>> ").upper()

# Splitting Date to Day, Month, and Year
dd, mm, yyyy = sesDate.split("-")
day = int(dd)
month = int(mm)
year = int(yyyy)
'''
# Determining the week number based on the session date
if 18 <= day <= 24 and month == 1:
    week = 1
elif 25 <= day <= 31 and month == 1:
    week = 2
elif 1 <= day <= 7 and month == 2:
    week = 3
elif 8 <= day <= 14 and month == 2:
    week = 4
elif 15 <= day <= 21 and month == 2:
    week = 5
elif 22 <= day <= 28 and month == 2:
    week = 6
elif 1 <= day <= 7 and month == 3:
    week = 7
elif 8 <= day <= 14 and month == 3:
    week = 8
elif 15 <= day <= 21 and month == 3:
    week = 9
elif 22 <= day <= 28 and month == 3:
    week = 10
elif (29 <= day <= 31 and month == 3) or (1 <= day <= 7 and month == 4):
    week = 11
elif 8 <= day <= 14 and month == 4:
    week = 12
elif 15 <= day <= 21 and month == 4:
    week = 13
else:
    week = 14
'''

if month == 1:
    DDC = day - 18
elif month == 2:
    DDC = 13 + day
elif month == 3:
    DDC = 41 + day
elif month == 4:
    DDC = 72 + day

week = DDC // 7 + 1
# Calculating Session Duration
hhS, mmS = map(int, sesStime.split(":"))
hhE, mmE = map(int, sesEtime.split(":"))
sesHrs = (hhE + (mmE / 60)) - (hhS + (mmS / 60))

# Output the session week and hours
print()
print(f"Session’s Week Number    : {week}")
print(f"Session’s Time in hrs    : {sesHrs:.1f}")
print(f"Student’s Name (year)    : {stuName} (20{stuID[0:2]})")
print()

# Collecting Access and Logout Times
accessT = input("Student’s access time    : ")
hha, mma = map(int, accessT.split(":"))
logoutT = input("Student’s logout time    : ")
hht, mmt = map(int, logoutT.split(":"))

# Calculating Attendance Duration in minutes
attendance = ((hht + mmt / 60) - (hha + mma / 60)) * 60
attendance = 5 * round(attendance / 5)  # Rounding to the nearest 5 minutes

# Output the total attendance time in minutes
print()
print(f"Total mins in attendance : {attendance}")
