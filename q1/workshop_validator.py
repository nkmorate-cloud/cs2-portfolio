name = input("Enter student name: ")

valid = True
error = ""

if not name:
    print("Student name is required.")
    exit()
  
while True:
    try:  
        age = int(input("Enter your age: "))
    except ValueError:
        print("Age must be a number.")
        exit()
    if age > 18:
        print("Age must be from 11 to 18.")
        exit()
    elif age < 11:
        print("Age must be from 11 to 18.")
        exit()
    break
grade = int(input("Enter your grade level: "))

if 12 < grade:
    print("Invalid grade level.")
    exit()
elif grade < 7:
    print("Invalid grade level.")
    exit()

email = input("Enter email: ").strip()
if valid:
    if "@" not in email or ".edu.ph" not in email:
        print("Invalid format.")
        exit()
  
code = input("Enter registration code: ").strip()
if valid:
    if len(code) != 6:
       print("The registration code must contain exactly 6 characters.")
       exit()

if valid:
    print("REGISTRATION ACCEPTED\n")
    print(f"Student: {name}")
    print(f"Age: {age}")
    print(f"Grade Level: {grade}")
    print(f"Email: {email}")
    print(f"Registration Code: {code}")
