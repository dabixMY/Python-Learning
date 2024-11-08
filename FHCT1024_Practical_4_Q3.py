"""
hazard_index = abs(int(input("Please enter pollutant hazard index: ")))

if 0 < hazard_index <= 100:
    print("healthy")
elif 100 < hazard_index <= 200:
    print("unhealthful")
elif 200 < hazard_index <= 275:
    print("first-stage haze alert")
else:
    print("second-stage alert")
"""

hazard_index = abs(int(input("Please enter pollutant hazard index: ")))

if hazard_index <= 100:
    print("Healthy")
elif hazard_index <= 200:
    print("Unhealthful")
elif hazard_index <= 275:
    print("First-stage haze alert")
else:
    print("Second-stage alert")