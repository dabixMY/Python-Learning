student_file = open("Student.txt", "w")

repeat = 'y'

while repeat.lower() == 'y':
    f_name = input("Enter first name >> ")
    l_name = input("Enter last  name >> ")
    stu_id = input("Enter student id >> ")
    age = int(input("Enter age       >> "))
    country = input("Enter country   >> ")

    student_file.write(f"{f_name}, {l_name}, {stu_id}, {age}, {country}\n")

    repeat = input("Do you want to key in next input? (y/n) >> ")

student_file.close()

print("File saved!")

view = 'y'

while view.lower() == 'y':
    # read the file from text file
    read_file = open("Student.txt", "r")

    key = input("Enter the search key word >> ")

    print(f"{"Name":^21} | {"Student ID":^10} | {"Age":^3} | {"Country":^10}")

    # access each line from the file
    for lines in read_file:
        # split each line into a list of items
        data = lines.split(',')
        if key in lines:
            print(f"{data[0]:<10} {data[1]:<10} | {data[2]:^10} | {int(data[3]):^3} | {data[4]:^10}")

    view = input("Do you want to make another search? (y/n) >> ")

    read_file.close()
