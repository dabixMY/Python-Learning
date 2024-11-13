hhStart, mmStart = map(int, input("Enter Starting Time (24-hour) : ").split(":"))
distance = float(input("Enter Distance travelled (km) : "))
velocity = float(input("Enter Average Velocity (km/hr): "))
print()

time = distance / velocity
hours = time // 24
mins = (time % 24 - hours) * 60

print(f"Time taken to travel    : {time // 24:.0f} day {hours:.0f} hour {mins:.0f} minutes ")

timeA = (hhStart + (mmStart / 60)) + time

if timeA >= 24:
    timeA = timeA - 24
else:
    timeA = timeA

hhA = timeA // 1
if hhA >= 12:
    hhA = hhA - 12
    ampm = "PM"
else:
    ampm = "AM"
mmA = (timeA - timeA // 1) * 60

print()
print(f"Arrival time            : {hhA:.0f}:{mmA:.0f} {ampm}")
