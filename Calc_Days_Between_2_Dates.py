start_date = "20240101"
end_date = "20250101"

start_year = int(start_date[:4])
start_month = int(start_date[4:6])
start_day = int(start_date[6:])

end_year = int(end_date[:4])
end_month = int(end_date[4:6])
end_day = int(end_date[6:])

daylst = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (start_year % 4 == 0 and start_year % 100 != 0) or (start_year % 400 == 0):
    daylst[2] = 29

start_days = 0
for m in range(1, start_month):
    start_days += daylst[m]
start_days += start_day

if (end_year % 4 == 0 and end_year % 100 != 0) or (end_year % 400 == 0):
    daylst[2] = 29

end_days = 0
for m in range(1, end_month):
    end_days += daylst[m]
end_days += end_day

total_start_days = 0
for y in range(1, start_year):
    total_start_days += 366 if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) else 365
total_start_days += start_days

total_end_days = 0
for y in range(1, end_year):
    total_end_days += 366 if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) else 365
total_end_days += end_days

print(abs(total_end_days - total_start_days))
