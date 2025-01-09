with open("inventory.txt", 'r') as file:
    lines = file.readlines()

rec = [x.strip("\n").split("|") for x in lines]

cont = 'y'

while cont == 'y':

    print("<1> Add new item  <2> Check inventory")
    selection = input("Insert your selection: ")
    print()

    if selection == '1':
        name =     input('Insert Item Name : ')
        price =    input('Insert Item Price: ')
        quantity = input('Insert Quantity  : ')

        with open('inventory.txt', 'a') as file:
            file.write('|'.join([name,price,quantity]) + "\n")
    elif selection == '2':
        print(f"{'Item Name':<15}{'Item Price (RM)':^15}{'Quantity':^15}")
        for record in rec:
            print(f'{record[0]:<15}{record[1]:^15}{record[2]:^15}')

        print('Item(s) need to be restocked: ')

        num = sum(1 for record in rec if int(record[2]) < 10)
        count = 1
        for record in rec:
            if int(record[2]) < 10:
                print(f"{count}. {record[0]} left {record[2]} unit(s).")
                count += 1

    cont = input("Press 'y' to continue or 'n' to quit: ")


