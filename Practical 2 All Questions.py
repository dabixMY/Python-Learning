import Global_Variable as SET
import os

def prac2Q1():
    # Conversion constant
    convConst = 3.2808

    # Function to convert feet to metres
    def feet2metres(vFeet):
        return vFeet / convConst

    # Function to convert metres to feet
    def metres2feet(vMetres):
        return vMetres * convConst

    # Step 2 -> input for feet
    feet = float(input("Insert feet   >> "))

    # Step 3 -> input for metres
    metres = float(input("Insert metres   >> "))

    # Convert feet to metres
    rMetres = feet2metres(feet)

    # Convert metres to feet
    rFeet = metres2feet(metres)

    # Print the results
    print("{:.2f} feet = {:.2f} metres".format(feet, rMetres))
    print("{:.2f} metres = {:.2f} feet".format(metres, rFeet))
    input()

# prac2Q1()

def prac2Q2():
    def calAvg1(no1, no2, no3, no4, no5):
        return (no1 + no2 + no3 + no4 + no5) / 5

    def calAvg2(numLst):
        return sum(numLst) / len(numLst)

    num1 = int(input("Enter 1st number >> "))
    num2 = int(input("Enter 2nd number >> "))
    num3 = int(input("Enter 3rd number >> "))
    num4 = int(input("Enter 4th number >> "))
    num5 = int(input("Enter 5th number >> "))

    avg1 = calAvg1(num1, num2, num3, num4, num5)
    avg2 = calAvg2([num1, num2, num3, num4, num5])

    print("Average of 5 numbers is : {:.2f}".format(avg1))
    input()

# prac2Q2()

def prac2Q3():
    def calArea(ht, wd, bs):
        aRec = ht * wd
        aSqu = ht ** 2
        aTri = (1 / 2) * bs * ht
        return aRec, aSqu, aTri

    ht = float(input("Insert Height Value : "))
    wd = float(input("Insert Width Value : "))
    bs = float(input("Insert Base Value : "))

    areaRec, areaSquare, areaTri = calArea(ht, wd, bs)
    print(f"Area of Rectangle is {areaRec}.")
    print(f"Area of Square is {areaSquare}.")
    print(f"Area of Triangle is {areaTri}.")
    input()

# prac2Q3()

def prac2Q4():
    def getcDesc(code):
        cLst = ['FHCT1024', 'FHCT1012']
        cDescLst = ['Programming Concepts and Design', 'Computing Technology']
        idx = cLst.index(code)
        return cDescLst[idx]

    def getGradeGP(marks):
        gpLst = [0] * 10 + [2.0, 2.33, 2.67, 3.0, 3.33, 3.67] + [4.0] * 5
        gradeLst = ['F'] * 10 + ['C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A', 'A+', 'A+', 'A+']
        gp = gpLst[marks // 5]
        grade = gradeLst[marks // 5]
        return gp, grade

    cCode1 = input("Enter course code >> ")
    print(getcDesc(cCode1))
    mrks1 = int(input("Enter marks    >>"))
    rgp1, rgrade1 = getGradeGP(mrks1)
    print("Grade :{:s}".format(rgrade1))

    cCode2 = input("Enter course code >> ")
    print(getcDesc(cCode2))
    mrks2 = int(input("Enter marks    >>"))
    rgp2, rgrade2 = getGradeGP(mrks2)
    print("Grade :{:s}".format(rgrade2))

    CH1 = int(cCode1[-1])
    CH2 = int(cCode2[-1])
    cgpa = (CH1 * rgp1 + CH2 * rgp2) / (CH1 + CH2)
    print("CGPA : {:.4f}".format(cgpa))
    input()

# prac2Q4()

def loginMenu():
    loop = True
    while loop:
        os.system('cls')
        print(SET.DASH)
        print("XXLibrary System - Login")
        print(SET.DASH)
        print("<1> Practical2 Q1")
        print("<2> Practical2 Q2")
        print("<3> Practical2 Q3")
        print("<4> Practical2 Q4")
        print("<Q> Quit System")
        print(SET.DASH)

        opt = input("Opt >> ")
        if opt == "Q":
            loop = False
            print("Program ends")
        elif opt == "1":
            prac2Q1()
        elif opt == "2":
            prac2Q2()
        elif opt == "3":
            prac2Q3()
        elif opt == "4":
            prac2Q4()
        else:
            print("Error, invalid input")
            input()

# Call the function
loginMenu()
