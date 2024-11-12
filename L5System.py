import os

#global variable
rec=[]

def addRec():
    eliLst=["Not eligible","Eligible"]
    studID  =      input("Enter Student ID           >> ")
    actScore=int(  input("Enter ACT Score            >> "))
    topHalf =      input("Enter topHalf (Y,Yes,N,No) >> ").upper()
    gpa     =float(input("Enter gpa                  >> "))

    idx=(actScore >=18 and topHalf in ["Y","YES"] or \
        actScore >=18 and gpa >=2.0 or \
        topHalf in ["Y","YES"] and gpa >=2.0)*1
    print("%s"%eliLst[idx])
    eligibility=eliLst[idx]
    rec.append([studID, actScore,topHalf,gpa,eligibility])

def displayRec(lRec):
    print("-"*60)
    print("RecNo  StudentID  ACTScore  TopHalf      GPA   Eligibilty")
    print("-"*60)
    if len(rec)==0:
        print("nil")
    else:
        for idx in range(len(rec)):
            print("%3d    %10s   %3d       %-5s   %6.4f   %s"%(idx+1,rec[idx][0],
                rec[idx][1],rec[idx][2],rec[idx][3], rec[idx][4]))
    print("-"*60)
    
def main():
    loop=True
    while loop:
        displayRec(rec)
        opt=input("<A>dd  <U>pdate  <D>elete  <S>ync  <Q>uit  >>").upper()
        if opt=="Q":
            loop=False
        elif opt in ["U","D","S"]:
            print("akan datang")
        elif opt in ["A"]:
            addRec()
        else:
            print("Invalid option entered")

if __name__=="__main__":
    main()
