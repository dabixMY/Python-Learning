
def sMain(cnt):
    for i in range(cnt):
        print(i, end = " ")
    print()
    #main()/sMain()

def main():
    n=5
    loop=True
    while loop:
        n=input("Enter number of times to repeat for loop >> ")
        if n=="Q":
            loop=False
        else:
            n=int(n)
            sMain(n)

main()
