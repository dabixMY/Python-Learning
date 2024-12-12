grade_list = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "F"]
point_list = [4.0, 4.0, 3.667, 3.333, 3.0, 2.667, 2.333, 2.0, 0.0]

result_list = []
total_point = 0
total_credit_hour = 0
CGPA = 0

repeat = True

student_id = input("Enter student code >> ")

while repeat:

    code  = input("Enter course code >> ").upper()

    if code.upper() == "Q":
        repeat = False
    else:
        grade = input("Enter grade       >> ").upper()

        result_list.append([student_id,code,grade])
with open("stuCGPA.txt","w") as f:

    for subject in result_list:
        f.write(f"\nCourse code: {subject[1]}")
        f.write(f"\nGrade: {subject[2]}")
        total_credit_hour += int(subject[1][-1])
        total_point += point_list[grade_list.index(subject[2])] * int(subject[1][-1])

    CGPA = total_point / total_credit_hour

    print(f"CGPA: {CGPA:.3f}")
    f.write(f"\nCGPA: {CGPA:.3f}")