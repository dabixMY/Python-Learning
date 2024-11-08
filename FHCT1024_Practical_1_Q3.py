"""
Sample Output:

Please enter student’s ID   : 20UHF00001
Please enter student’s name : John Kelvin
Number of courses registered: 4
Course 1: FHCT1024
Course 2: FHMM1034
Course 3: FHSC1234
Course 4: FHEL1012


--------------------------------------------------------
Student(id/name): 20UHF00001/John Kelvin
--------------------------------------------------------
Courses taken   : FHCT1024, FHMM1034, FHSC1234, FHEL1012
Total credit hours:14

"""
stuID = input("Please enter student’s ID   : ").upper().strip()
stuNAME = input("Please enter student’s name : ").strip().title()

while True:
    try:
        num_courses = int(input("Number of courses registered: "))
        break
    except ValueError:
        pass

# Create a list to store course codes
courses = []

# Loop to collect course codes
for i in range(num_courses):
    course_code = input(f"Course {i + 1}: ").upper().strip() # Convert input to uppercase and remove whitespace
    courses.append(course_code) # append() is a simple way to keep adding items to a list as you gather them.

print("--------------------------------------------------------")
print("Student(id/name): ", stuID+"/"+stuNAME)
print("--------------------------------------------------------")

""" 
If you simply want to print the whole list without formatting, you can do this:
print("Courses taken   : ", courses)
Sample Output:
Courses Registered: ['FHCT1024', 'FHMM1034', 'FHEL1012']
"""

print("Courses taken   : "+", ".join(courses)) #Use join() for a clean, comma-separated string of the courses.

# Create a list to store the credit hours extracted from each course code
credit_hr_list = []

# Loop through each course code and extract the last character
for course_code in courses:
    credit_hr = float(course_code[-1]) # Extract the last character and convert to float
    credit_hr_list.append(credit_hr) # Add to the credit hours list

sum_credit_hr = sum(credit_hr_list)

print("Total credit hours:",sum_credit_hr)


