rec = []
loop = True
while loop:
    ic = input("Enter NRIC number >> ")
    if ic == "HALT":
        loop = False
    # elif not validIC():
    #     print("Error with IC entered")
    else:
        totPurc = float(input("Enter total purchase >> "))
        # method 1 - identify if this is repeated
        if ic is [x[0] for x in rec]:
            idx = [x[0] for x in rec].index(ic)
            rec[idx][1] += totPurc
        else:
            # method 2 - append all records
            rec.append([ic,totPurc])

# method 1
m1Lst =[[x[1],x[0]] for x in rec]
m1Lst.sort(reverse=True)
# for ppl in m1Lst(3):
print(m1Lst[:3])

# method 2
icULst = list(set([x[0] for x in rec]))
sRec = []
for i in range(len(icULst)):
    purc = sum(x[1] for x in rec if x[0] == icULst[i])
    sRec.append([purc,icULst[i]])
sRec.sort(reverse=True)
#for ppl in sRec:
print(sRec[:3])