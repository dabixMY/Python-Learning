numLst = []
squareLst = []

repeat = True

while repeat:
    number = int(input("Enter number (0 to stop) >> "))

    if number == 0:
        repeat = False
    else:
        numLst.append(number)
        squareLst.append(number**2)

print("Number  |  Square")

for count in range(len(numLst)):
    print(f"{numLst[count]:6d}  |  {squareLst[count]:6d}")
