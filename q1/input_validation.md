# Input Validation and Output Verification 
**Activity:** PSHS Workshop Registration Validator 

**Name:** NEIDGEL KATE MORATE

**Section:** 8-Dahlia 

**Quarter:** 1 
--- 
## Activity Overview 
In this activity, I created a program that validates information entered into a PSHS workshop registration system. 
The program checks whether user input satisfies specific requirements before accepting the registration. The program validates: 
- student name 
- age 
- grade level 
- email address and 
- registration code.
--- 
# Part A - Validation Requirements 
Complete the table below before writing your program. 
| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error Message | 
|---|---|---|---|---|---| 
| Student Name | String | Presence | "" | Must not be empty or blank | Student name is required. | 
| Age | Integer | Data Type + Range | "twelve", 24 | Must be an integer AND between 11 and 18 | "Age must be a number.", "Age must be from 11 to 18." | 
| Grade Level | Integer | Acceptable value | 6, 13 | Must belong to the list: 7, 8, 9, 10, 11, 12 | "Invalid grade level." | 
| Email Address | String | Pattern | student.pshs.edu.ph | Must contain ".edu.ph" AND the @ character | Invalid email format. |
| Registration Code | CodeString | Length | A123 | Length of the string must equal exactly 6 | "The registration code must contain exactly 6 characters." | 
--- 
## Validation Questions
### 1. Why should the student name not be blank? 
> A blank name makes it impossible to identify who the student is. 
### 2. Why should age be checked for both data type and range? 
> Checking the data type prevents the program from crashing when converting text like "fourteen" into a number. Checking the range ensures valid age inputs.
### 3. Why should grade level only accept specific values? 
> This highschool only has grade levels 7-12. Only accepting these specific values blocks invalid responses. 
### 4. What format requirements did you use for the email address? 
> A simple string pattern check requiring the input to contain ".edu.ph" and at least one @ character. 
### 5. What length requirement did you use for the registration code? 
> The code must contain exactly 6 characters.  Anything else that's under or over the limit is invalid.
--- 
# Part B - Program Design 
```
START

  // Input and validate Student Name
  READ name
  IF name is empty THEN
    DISPLAY "Student name is required."
    EXIT program
  ENDIF

  // Input and validate Age (Loop until a valid number between 11 and 18 is given)
  WHILE true DO
    READ age_input
    IF age_input is not a valid number THEN
      DISPLAY "Age must be a number."
      CONTINUE loop
    ENDIF
    
    CONVERT age_input to integer age
    
    IF age < 11 OR age > 18 THEN
      DISPLAY "Age must be from 11 to 18."
      CONTINUE loop
    ELSE
      BREAK loop // Age is valid, exit the loop
    ENDIF
  ENDWHILE

  // Input and validate Grade Level
  READ grade
  IF grade < 7 OR grade > 12 THEN
    DISPLAY "Invalid grade level."
    EXIT program
  ENDIF

  // Input and validate Email
  READ email
  IF email does not contain "@" OR does not contain ".edu.ph" THEN
    DISPLAY "Invalid format."
    EXIT program
  ENDIF

  // Input and validate Registration Code
  READ code
  IF length of code is not equal to 6 THEN
    DISPLAY "The registration code must contain exactly 6 characters."
    EXIT program
  ENDIF

  // Display Registration Details
  DISPLAY "REGISTRATION ACCEPTED"
  DISPLAY "Student: " + name
  DISPLAY "Age: " + age
  DISPLAY "Grade Level: " + grade
  DISPLAY "Email: " + email
  DISPLAY "Registration Code: " + code
```

END
# Part C - Program Implementation 
## Programming Language 
> Python 
## Source Code File 
[workshop_validator.py](workshop_validator.py) 
## Final Code 
```python 
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
``` 
--- 
## Validation Techniques Used 
### Presence Validation 
Explain where you used presence validation. 
> Write your answer here. 
### Data Type Validation 
Explain where you used data type validation. 
> Write your answer here. 
### Range Validation 
Explain where you used range validation. 
> Write your answer here.
### Acceptable Value Validation 
Explain where you used acceptable value validation. 
> Write your answer here. 
### Pattern Validation 
Explain the simple pattern rule you used. 
> Write your answer here. 
### Length Validation 
Explain the length rule you used. 
> Write your answer here. 
--- 
# Part D - Testing 
Test your program using both valid and invalid inputs. 
| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result | 
|---:|---|---|---|---|---| 
| 1 | All inputs valid | Normal case | | | | 
| 2 | Blank student name | Presence | | | | 
| 3 | Age = `fourteen` | Data type | | | | 
| 4 | Age = `11` | Minimum boundary | | | | 
| 5 | Age = `18` | Maximum boundary | | | | 
| 6 | Age = `10` | Range | | | | 
| 7 | Grade Level = `13` | Acceptable value | | | | 
| 8 | Email = `studentpshs.edu.ph` | Pattern | | | | 
| 9 | Registration Code = `ABC` | Length | | | | 
| 10 | Registration Code = `CS2026` | Valid length | | | | 
Write **PASS** when the actual output matches the expected output. 
Write **FAIL** when it does not. 
--- 
# Part E - Output Verification 
Choose any **three tests** from Part D. 
## Verification Test 1 
**Input:** 
```text 
Write the input here.
``` 
**Expected Output:** 
```text 
Write the expected output here. 
``` 
**Actual Output:** 
```text 
Write the actual output here. 
``` 
**Result:** PASS / FAIL 
**Explanation:** 
> Explain why the output is correct or incorrect. --- 
## Verification Test 2 
**Input:** 
```text 
Write the input here. 
``` 
**Expected Output:** 
```text 
Write the expected output here. 
``` 
**Actual Output:** 
```text 
Write the actual output here. 
``` 
**Result:** PASS / FAIL 
**Explanation:** 
> Explain why the output is correct or incorrect. --- 
## Verification Test 3 
**Input:** 
```text 
Write the input here. 
``` 
**Expected Output:** 
```text 
Write the expected output here. 
``` 
**Actual Output:**
```text 
Write the actual output here. 
``` 
**Result:** PASS / FAIL 
**Explanation:** 
> Explain why the output is correct or incorrect. 
--- 
# Reflection 
Answer briefly. 
### 1. Why should a program validate input before processing it? 
> Write your answer here. 
### 2. What is the difference between input validation and output verification? 
> Write your answer here. 
### 3. Which validation technique was easiest for you to implement? Why? 
> Write your answer here. 
### 4. Which validation technique was most challenging? Why? 
> Write your answer here. 
### 5. How did testing invalid inputs help you improve your program? 
> Write your answer here. 
--- 
