"""
Display the following outputs.

HELLO WORLD ^_^

Name    : [Own Detail]
Age     : [Own Detail]
Hometown: [Own Detail]

    *
   ***
  *****
 *******
*********
"""

name = input("PLEASE ENTER YOUR NAME: ").strip().title() #combine two functions

#name = name.strip() #Remove whitespace from str
#name = name.title() # Output: desmond tay qi shun -> Desmond Tay Qi Shun
#name = name.capitalize() # Output: desmond tay -> Desmond tay qi shun

while True:
    try:
        age = int(input("PLEASE ENTER YOUR AGE AS A NUMBER: "))
        break # Exit loop if input is valid
    except ValueError:
        print("PLEASE ENTER YOUR AGE AS A NUMBER, NOT LETTERS.")

hometown = input("PLEASE ENTER YOUR HOMETOWN: ").strip().title()

print()
print("HELLO WORLD ^_^")
print()
print("Name    :", name)
print("Age     :", age)
print("Hometown:", hometown)
print()

rows = 5
for i in range(rows):
    print(' ' * (rows - i - 1) + '*' * (2 * i + 1))
