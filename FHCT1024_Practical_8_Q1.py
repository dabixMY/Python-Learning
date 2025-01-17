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

    if code.lower() == "halt":
        repeat = False
    else:
        grade = input("Enter grade       >> ").upper()

        result_list.append([student_id,code,grade])

print(result_list)

for subject in result_list:
    print(f"credit hour: {int(subject[1][-1])}")
    print(f"grade point: {point_list[grade_list.index(subject[2])]:.2f}")
    total_credit_hour += int(subject[1][-1])
    total_point += point_list[grade_list.index(subject[2])] * int(subject[1][-1])

CGPA = total_point / total_credit_hour
print(f"CGPA: {CGPA:.3f}")