import datetime

nric1 = input("Enter NRIC number 1 (YYMMDD-PB-####) >> ")
nric2 = input("Enter NRIC number 2 (YYMMDD-PB-####) >> ")
print()

a1, b1, c1 = nric1.split("-")
a2, b2, c2 = nric2.split("-")

year1, month1, day1 = a1[0:2], a1[2:4], a1[4:6]
year2, month2, day2 = a2[0:2], a2[2:4], a2[4:6]

months = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "May",
    "06": "Jun",
    "07": "Jul",
    "08": "Aug",
    "09": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec"
}

month1 = months.get(month1)
month2 = months.get(month2)

today = datetime.date.today()

years = int(today.year)
year1 = int(year1)
year2 = int(year2)

# Calculate age
if 24 <= year1 <= 99:
    age1 = years - (1900 + year1)
else:
    age1 = years - (2000 + year1)

if 24 <= year2 <= 99:
    age2 = years - (1900 + year2)
else:
    age2 = years - (2000 + year2)

# Determine gender
if int(c1[-1]) % 2 == 0:
    gender1 = "Female"
else:
    gender1 = "Male"

if int(c2[-1]) % 2 == 0:
    gender2 = "Female"
else:
    gender2 = "Male"

print("NRIC Number       BirthDate     Age     Gender")
print("-" * 50)
print(f"{nric1}    {day1:2s} {month1:3s} {a1[0:2]:2s}     {age1:2d}      {gender1:6s}")
print(f"{nric2}    {day1:2s} {month2:3s} {a2[0:2]:2s}     {age2:2d}      {gender2:6s}")