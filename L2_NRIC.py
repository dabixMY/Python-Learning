NRIC = input("Enter your IC number in format YYMMDD-SS-NNNN : ")
a,b,c = NRIC.split("-")

nric= int(a)

year = a[0:2]
month = a[2:4]
day = a[4:6]

bulan = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

month=bulan.get(month)

tahun= int (year)

if tahun <= 24:
    century="20"
else:
    century="19"

if day in ["11","12","13"]:
    ordinal="th"
else:
    if a[-1]=="1":
        ordinal="st"
    elif a[-1]=="2":
        ordinal="nd"
    elif a[-1]=="3":
        ordinal="rd"
    else:
        ordinal="th"

print(day+ordinal, month, century+year)

if int(c[-1])%2 == 0:
    print("Female")
else:
    print("Male")