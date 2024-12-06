grade_list = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "F"]
point_list = [4.0,4.0,3.667,3.333,3.0,2.667,2.333,2,0]

student_list = []

student_id = input("Enter student code >> ")

repeat = True

while repeat:

    code  = input("Enter course code >> ")

    if code != "halt":
        grade = input("Enter grade       >> ")

        student_list.append([student_id,code,grade])

        credit_hour = code[-1]
        print(credit_hour)
        print(point_list[grade_list.index(grade)])

    else:
        repeat = False

print(student_list)

