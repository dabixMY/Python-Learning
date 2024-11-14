saving = 5000
year = 0

print("Year     Saving")

while saving < 10000:
    #saving = saving * 1.02
    saving *= 1.02
    #year = year + 1
    year += 1
    print(f" {year:2d} : RM {saving:10.2f}")

print(f"It takes {year} years to reach the target.")
