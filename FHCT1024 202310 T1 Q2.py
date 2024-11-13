import math

d = float(input("Enter distance (KM)    >> "))
v = float(input("Enter velocity (KM/hr) >> "))

t = (d * 1.02 ** 2) / (math.cbrt(1.005) * v) + 0.125 / (d * 0.01)
t = t * 60
print(f"Total time in minutes   : {t:.5f}")

if t >= 1440:
    days = t // 1440
    hours = (t / 1440 - days) * 24
    mins = (hours - int(hours)) * 60
else:
    days = 0
    hours = t // 60
    mins = (t / 60 - hours) * 60

print(f"Time taken to travel    : {days:.0f} day(s) {hours:.0f} hours {mins:.0f} mins")
print()

petrol = input("Petrol Used            >> ").upper()
carCC = int(input("Car cc                 >> "))

if petrol == "RON95":
    RMperL = 2.05
elif petrol == "RON97":
    RMperL = 3.47

if carCC == 1500:
    kmph = 18.518518
elif carCC == 2000:
    kmph = 12.820512

totCost = (d / kmph) * RMperL
costAdj = round(totCost * 20) / 20

print(f"Total cost              :RM    {costAdj:.2f}")

if costAdj < totCost:
    print(f"Adjustment              :RM     -{totCost - costAdj:.2f}")
    print(f"Total after adjustment  :RM    {costAdj:.2f}")
else:
    print(f"Adjustment              :RM     +{costAdj - totCost:.2f}")
    print(f"Total after adjustment  :RM    {costAdj:.2f}")