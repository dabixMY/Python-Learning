
#step1
import Global_Variable as SET #self-defined module
import os             #standard io module

#syntax -> def functionName (arguments):

def prac2Q1():
    print("Akan datang")
    input()
def prac2Q2():
    print("Akan datang")
    input()

def loginMenu():
    loop=True
    while loop:
        os.system('cls')
        print(SET.DASH)
        print("XXLibrary System - Login")
        print(SET.DASH)
        print("<1>Practical2 Q1")
        print("<2>Practical2 Q2")
        print("<Q>uit System")
        print(SET.DASH)
        opt=input("Opt >> ")
        if opt=="Q":
            loop=False
            print("program ends")
        elif opt=="1":
            prac2Q1()
        elif opt=="2":
            prac2Q2()
        else:
            print("Error, invalid input")
            input()

#step2
loginMenu()
