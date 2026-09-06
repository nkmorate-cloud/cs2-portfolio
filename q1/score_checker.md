# Clean Decision Code Makeover: Student Score Checker 
**Name:** NEIDGEL KATE MORATE
**Section:** 8-Dahlia
--- 
## Activity Overview 
In this activity, I improved a Student Score Checker program by applying proper coding standards and selection structures. 
The program accepts a student score from 0 to 100 and determines the appropriate classification. 
The classifications are: 
| Score | Classification | 
|---:|---| 
| 90–100 | Outstanding | 
| 80–89 | Very satisfactory | 
| 75-79 | Satisfactory | 
| 0–74 | Needs Improvement | 
| Scores below 0 or above 100 | considered invalid. |
--- 

# 1
Input: What information does the program need?  
* The student's score (or numbers representing their score)

Boundary: What is the minimum valid score?
* 0

Boundary: What is the maximum valid score?
* 100

Possible Outputs: What outcomes can the program produce? 
* Invalid score (for scores below 0 and above 100),  Outstanding (for scores between 90 and 100), Very satisfactory (for scores between 80 and 89), Satisfactory (for scores between 75 and 79), Needs improvement (for scores below 75)

Selection Pattern: Which part uses a boundary condition?
* (if score < 0 or score > 100:) uses boundary conditions 

Selection Pattern: Which part uses multiple decision paths?
* (elif score >= 90: ... elif score >= 80: ... else:) uses multiple decision paths

# 2
* [ START ]
*           │
*           ▼
*     / INPUT score /
*           │
*           ▼
*     /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
*    < score < 0 OR > 100?    > ─── Yes ───► [ DISPLAY "Invalid score" ]
*     \______________________/                       │
*           │ No                                     │
*           ▼                                        │
*     /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\                       │
*    <      score >= 90?      > ─── Yes ───► [ DISPLAY "Outstanding" ]
*     \______________________/                       │
*           │ No                                     │
*           ▼                                        │
*     /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\                       │
*    <      score >= 80?      > ─── Yes ───► [ DISPLAY "Very Satisfactory" ]
*     \______________________/                       │
*           │ No                                     │
*           ▼                                        │
*     /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\                       │
*    <      score >= 75?      > ─── Yes ───► [ DISPLAY "Satisfactory" ]
*     \______________________/                       │
*           │ No                                     │
*           ▼                                        │
*    [ DISPLAY "Needs Improvement" ]                 │
*           │                                        │
*           ▼                                        ▼
*           └───────────────────────────────────────►[ END ]


# 3
* START
* INPUT score

* IF score < 0 OR score > 100 THEN
*    DISPLAY "Invalid score"
* ELSE IF score >= 90 THEN
*    DISPLAY "Outstanding"
* ELSE IF score >= 80 THEN
*    DISPLAY "Very Satisfactory"
* ELSE IF score >= 75 THEN
*    DISPLAY "Satisfactory"
* ELSE
*    DISPLAY "Needs Improvement"
* END

# 4
[Score Checker Source Code](score_checker.py).

# 5
| Test | Input | Purpose | Expected Output | Actual Output | Result | 
|---|---:|---|---|---|---| 
| 1 | -1 | Below minimum | Invalid score | Invalid score | PASS | 
| 2 | 0 | Minimum boundary | Needs Improvement | Needs Improvement | PASS | 
| 3 | 74 | Below Satisfactory boundary | Needs Improvement | Needs Improvement | PASS | 
| 4 | 75 | Satisfactory boundary | Satisfactory | Satisfactory | PASS | 
| 5 | 80 | Very Satisfactory boundary | Very Satisfactory | Very Satisfactory | PASS | 
| 6 | 90 | Outstanding boundary | Outstanding | Outstanding | PASS | 
| 7 | 100 | Maximum boundary | Outstanding | Outstanding | PASS | 
| 8 | 101 | Above maximum | Invalid score | Invalid score | PASS | 

---
## Testing Reflection 
### 1. Why is it important to test the values 0 and 100? 
> They represent the minimum and maximum boundaries of a valid input.
### 2. Why did you also test -1 and 101? 
> They help test to see if it gives correct input for numbers outside the valid input boundary.
### 3. Which test helped you understand boundary conditions the most? 
> The tests with the output as "invalid score", it shows how the code treats numbers outside the valid input boundary.
### 4. Did any of your tests initially fail? If yes, what did you change in your program? 
> Yes, testing -1 failed. The program displayed both "Invalid Score" and "Needs Improvement" at the same time. I fixed it by putting "exit()" to exit the program without displaying the second print. 
--- 
# Reflection 
### 1. How did selection structures make the program more useful? 
> They allowed the program to process specific inputs. Without it, the system could not categorize invalid inputs. 
### 2. How did proper comments and readable formatting improve your program? 
> It helped organize the code and made it more easier to understand how it works. 
### 3. Why is it useful to plan the program using a flowchart and pseudocode before writing the code? 
> It helps avoid errors and plans out the code
