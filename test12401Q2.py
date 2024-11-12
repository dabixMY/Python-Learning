import calendar

regNum = input("Enter car registration no >> ")
timeIn = input("Enter car entry time [HH:MM] >> ")
timeOut = input("Enter car exit time [HH:MM] >> ")

hhIn, mmIn = timeIn.split(":")
hhIn = int(hhIn)
mmIn = int(mmIn)

hhOut, mmOut = timeOut.split(":")
hhOut = int(hhOut)
mmOut = int(mmOut)

time_interval = (hhOut * 60 + mmOut) - (hhIn * 60 + mmIn)
HH = time_interval // 60
MM = time_interval % 60

totHH = (HH == 0 and MM < 15) * 0 + (HH == 0 and MM >= 15) * 1 + (HH > 0 and MM > 0) * 1 + HH

chargesLst = [3, 2, 2, 2, 2, 2, 2, 2] + [0] * 15
charges = sum(chargesLst[:totHH])
print(f"Fees payable: RM {charges:.2f}")
print()

a, b, c = input("Enter date (dd/mm/yyyy) >> ").split("/")
print()

if calendar.weekday(int(c), int(b), int(a)) == 5 or calendar.weekday(int(c), int(b), int(a)) == 6:
    charges = 5
    if calendar.weekday(int(c), int(b), int(a)) == 5:
        print("Total parking fee on SAT is at: RM 5.00")
    else:
        print("Total parking fee on SUN is at: RM 5.00")
else:
    charges = charges
print()

paid = int(input("Amount paid >> RM "))
print("<-Change amount->")
print("<--------------->")

change = paid - charges
change50 = change % 50
change20 = change50 % 20
change10 = change20 % 10
change5 = change10 % 5
change2 = change5 % 2
change1 = change2 % 1

print(f"RM 50 x {change // 50} = {50 * (change // 50)}")
print(f"RM 20 x {change50 // 20} = {20 * (change50 // 20)}")
print(f"RM 10 x {change20 // 10} = {10 * (change20 // 10)}")
print(f"RM  5 x {change10 // 5} = {5 * (change10 // 5)}")
print(f"RM  2 x {change5 // 2} = {2 * (change5 // 2)}")
print(f"RM  1 x {change2} = {change2}")
