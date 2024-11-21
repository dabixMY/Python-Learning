repeat = True

while repeat:
    time_24 = int(input("Time in 24 hrs format >> "))

    if time_24 == 9999:
        repeat = False
    else:
        if time_24 % 100 >= 60:
            print("Minutes cannot be more than or equal to 60")
        elif 0 <= time_24 <= 59:
            time_12 = time_24 / 100 + 12
            print(f"Time in 12 hrs format : {time_12:.2f} am")
        elif 100 <= time_24 <= 1159:
            time_12 = time_24 / 100
            print(f"Time in 12 hrs format : {time_12:.2f} am")
        elif 1200 <= time_24 <= 1259:
            time_12 = time_24 / 100
            print(f"Time in 12 hrs format : {time_12:.2f} pm")
        elif 1300 <= time_24 <= 2359:
            time_12 = time_24 / 100 - 12
            print(f"Time in 12 hrs format : {time_12:.2f} pm")
        else:
            print("Input time is out of range, please key in again.")